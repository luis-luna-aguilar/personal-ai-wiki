from __future__ import annotations

from dataclasses import asdict
from typing import Any
import json
import re

from .schema import ExtractedAction, ExtractedEntity, ExtractedRelationship, ExtractedSection, ExtractedWorkflow


NAMESPACE = "ai-wiki-ontology"


def canonical_id(name: str, kind: str = "Thing") -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return normalized or re.sub(r"[^a-z0-9]+", "-", kind.lower()).strip("-") or "thing"


class Neo4jOntologyStore:
    def __init__(self, uri: str, user: str, password: str, database: str = "neo4j") -> None:
        try:
            from neo4j import GraphDatabase
        except ImportError as exc:
            raise RuntimeError("Install the neo4j package before using the ontology graph store.") from exc
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.database = database

    def close(self) -> None:
        self.driver.close()

    def verify(self) -> None:
        self.driver.verify_connectivity()

    def setup(self) -> None:
        queries = [
            "CREATE CONSTRAINT ontology_entity_id IF NOT EXISTS FOR (n:OntologyEntity) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT ontology_file_path IF NOT EXISTS FOR (n:OntologyFile) REQUIRE n.path IS UNIQUE",
            "CREATE CONSTRAINT ontology_batch_id IF NOT EXISTS FOR (n:OntologyBatch) REQUIRE n.id IS UNIQUE",
            "CREATE CONSTRAINT ontology_type_id IF NOT EXISTS FOR (n:OntologyType) REQUIRE n.id IS UNIQUE",
        ]
        with self.driver.session(database=self.database) as session:
            for query in queries:
                session.run(query)

    def clear_namespace(self) -> None:
        with self.driver.session(database=self.database) as session:
            session.run(
                "MATCH (n {namespace: $namespace}) DETACH DELETE n",
                namespace=NAMESPACE,
            )

    def delete_file_output(self, path: str) -> None:
        with self.driver.session(database=self.database) as session:
            session.run(
                """
                MATCH (f:OntologyFile {namespace: $namespace, path: $path})-[:PRODUCED_BATCH]->(b:OntologyBatch)
                OPTIONAL MATCH (b)-[owned_rel:MENTIONS]->(:OntologyEntity)
                DELETE owned_rel
                WITH b
                DETACH DELETE b
                """,
                namespace=NAMESPACE,
                path=path,
            )
            session.run(
                """
                MATCH ()-[r:RELATES {namespace: $namespace, source_path: $path}]->()
                DELETE r
                """,
                namespace=NAMESPACE,
                path=path,
            )
            session.run(
                """
                MATCH (f:OntologyFile {namespace: $namespace, path: $path})
                DETACH DELETE f
                """,
                namespace=NAMESPACE,
                path=path,
            )
            session.run(
                """
                MATCH (e:OntologyEntity {namespace: $namespace})
                WHERE NOT (e)<-[:MENTIONS]-(:OntologyBatch {namespace: $namespace})
                  AND NOT (e)--(:OntologyEntity {namespace: $namespace})
                DETACH DELETE e
                """,
                namespace=NAMESPACE,
            )

    def write_file_extraction(
        self,
        path: str,
        title: str,
        content_hash: str,
        batch_id: str,
        extracted_sections: list[ExtractedSection],
    ) -> None:
        with self.driver.session(database=self.database) as session:
            session.execute_write(
                self._write_file_extraction_tx,
                path,
                title,
                content_hash,
                batch_id,
                extracted_sections,
            )

    @staticmethod
    def _write_file_extraction_tx(
        tx: Any,
        path: str,
        title: str,
        content_hash: str,
        batch_id: str,
        extracted_sections: list[ExtractedSection],
    ) -> None:
        tx.run(
            """
            MERGE (f:OntologyFile {namespace: $namespace, path: $path})
            SET f.title = $title, f.content_hash = $content_hash
            MERGE (b:OntologyBatch {namespace: $namespace, id: $batch_id})
            SET b.path = $path
            MERGE (f)-[:PRODUCED_BATCH]->(b)
            """,
            namespace=NAMESPACE,
            path=path,
            title=title,
            content_hash=content_hash,
            batch_id=batch_id,
        )
        for extracted in extracted_sections:
            for entity in extracted.entities:
                _merge_entity(tx, entity, batch_id)
            for action in extracted.actions:
                _merge_action(tx, action, batch_id)
            for workflow in extracted.workflows:
                _merge_workflow(tx, workflow, batch_id)
            for relationship in extracted.relationships:
                _merge_relationship(tx, relationship, batch_id, path)
            for workflow in extracted.workflows:
                _merge_workflow_steps(tx, workflow, batch_id, path)
            for action in extracted.actions:
                _merge_action_io(tx, action, batch_id, path)

    def search(self, query: str, limit: int = 10) -> list[dict[str, Any]]:
        term = query.lower()
        with self.driver.session(database=self.database) as session:
            result = session.run(
                """
                MATCH (n:OntologyEntity {namespace: $namespace})
                WHERE toLower(n.name) CONTAINS $term
                   OR toLower(coalesce(n.summary, "")) CONTAINS $term
                   OR toLower(coalesce(n.properties_json, "")) CONTAINS $term
                OPTIONAL MATCH (n)-[r:RELATES {namespace: $namespace}]-(m:OntologyEntity {namespace: $namespace})
                RETURN n, collect({type: r.rel_type, neighbor: m.name, neighbor_kind: m.kind})[0..8] AS relationships
                LIMIT $limit
                """,
                namespace=NAMESPACE,
                term=term,
                limit=limit,
            )
            return [_record_to_dict(record) for record in result]

    def expand(self, name: str, depth: int = 2, limit: int = 30) -> list[dict[str, Any]]:
        with self.driver.session(database=self.database) as session:
            result = session.run(
                """
                MATCH (start:OntologyEntity {namespace: $namespace})
                WHERE toLower(start.name) = toLower($name)
                   OR any(alias IN start.aliases WHERE toLower(alias) = toLower($name))
                MATCH path = (start)-[:RELATES*1..2]-(neighbor:OntologyEntity {namespace: $namespace})
                RETURN start.name AS start, [rel IN relationships(path) | rel.rel_type] AS rel_types,
                       [node IN nodes(path) | {name: node.name, kind: node.kind}] AS nodes
                LIMIT $limit
                """,
                namespace=NAMESPACE,
                name=name,
                limit=limit,
            )
            return [dict(record) for record in result]

    def actions(self, goal: str, limit: int = 10) -> list[dict[str, Any]]:
        term = goal.lower()
        with self.driver.session(database=self.database) as session:
            result = session.run(
                """
                MATCH (n:OntologyEntity {namespace: $namespace})
                WHERE (n:OntologyAction OR n:OntologyWorkflow)
                  AND (
                    toLower(n.name) CONTAINS $term
                    OR toLower(coalesce(n.summary, "")) CONTAINS $term
                    OR toLower(coalesce(n.properties_json, "")) CONTAINS $term
                  )
                OPTIONAL MATCH (n)-[r:RELATES {namespace: $namespace}]->(m:OntologyEntity {namespace: $namespace})
                WHERE r.rel_type IN ["HAS_STEP", "REQUIRES", "PRODUCES", "BLOCKED_BY", "MITIGATED_BY"]
                RETURN n, collect({type: r.rel_type, neighbor: m.name, neighbor_kind: m.kind, order: r.order})[0..12] AS relationships
                LIMIT $limit
                """,
                namespace=NAMESPACE,
                term=term,
                limit=limit,
            )
            return [_record_to_dict(record) for record in result]


def _merge_entity(tx: Any, entity: ExtractedEntity, batch_id: str) -> None:
    entity_id = canonical_id(entity.name, entity.kind)
    tx.run(
        """
        MERGE (e:OntologyEntity {namespace: $namespace, id: $id})
        SET e.name = $name,
            e.kind = $kind,
            e.aliases = $aliases,
            e.summary = $summary,
            e.properties_json = $properties_json
        MERGE (t:OntologyType {namespace: $namespace, id: $type_id})
        SET t.name = $kind, t.category = "entity"
        MERGE (e)-[:HAS_TYPE]->(t)
        WITH e
        MATCH (b:OntologyBatch {namespace: $namespace, id: $batch_id})
        MERGE (b)-[:MENTIONS]->(e)
        """,
        namespace=NAMESPACE,
        id=entity_id,
        name=entity.name,
        kind=entity.kind,
        aliases=entity.aliases,
        summary=entity.summary,
        properties_json=json.dumps(entity.properties, sort_keys=True),
        type_id=f"entity:{entity.kind.lower()}",
        batch_id=batch_id,
    )


def _merge_action(tx: Any, action: ExtractedAction, batch_id: str) -> None:
    entity = ExtractedEntity(action.name, action.kind, [], action.properties)
    _merge_entity(tx, entity, batch_id)
    tx.run(
        """
        MATCH (e:OntologyEntity {namespace: $namespace, id: $id})
        SET e:OntologyAction
        """,
        namespace=NAMESPACE,
        id=canonical_id(action.name, action.kind),
    )


def _merge_workflow(tx: Any, workflow: ExtractedWorkflow, batch_id: str) -> None:
    entity = ExtractedEntity(workflow.name, workflow.kind, [], workflow.properties)
    _merge_entity(tx, entity, batch_id)
    tx.run(
        """
        MATCH (e:OntologyEntity {namespace: $namespace, id: $id})
        SET e:OntologyWorkflow
        """,
        namespace=NAMESPACE,
        id=canonical_id(workflow.name, workflow.kind),
    )


def _merge_relationship(tx: Any, relationship: ExtractedRelationship, batch_id: str, path: str) -> None:
    source_id = canonical_id(relationship.source)
    target_id = canonical_id(relationship.target)
    rel_type = _normalize_rel_type(relationship.rel_type)
    tx.run(
        """
        MERGE (source:OntologyEntity {namespace: $namespace, id: $source_id})
        ON CREATE SET source.name = $source_name, source.kind = "Thing", source.aliases = [], source.properties_json = "{}"
        MERGE (target:OntologyEntity {namespace: $namespace, id: $target_id})
        ON CREATE SET target.name = $target_name, target.kind = "Thing", target.aliases = [], target.properties_json = "{}"
        MERGE (rt:OntologyType {namespace: $namespace, id: $type_id})
        SET rt.name = $rel_type, rt.category = "relationship"
        MERGE (source)-[r:RELATES {namespace: $namespace, rel_type: $rel_type, source_path: $path}]->(target)
        SET r.properties_json = $properties_json,
            r.batch_id = $batch_id
        WITH source, target
        MATCH (b:OntologyBatch {namespace: $namespace, id: $batch_id})
        MERGE (b)-[:MENTIONS]->(source)
        MERGE (b)-[:MENTIONS]->(target)
        """,
        namespace=NAMESPACE,
        source_id=source_id,
        source_name=relationship.source,
        target_id=target_id,
        target_name=relationship.target,
        rel_type=rel_type,
        type_id=f"relationship:{rel_type.lower()}",
        properties_json=json.dumps(relationship.properties, sort_keys=True),
        batch_id=batch_id,
        path=path,
    )


def _merge_workflow_steps(tx: Any, workflow: ExtractedWorkflow, batch_id: str, path: str) -> None:
    workflow_id = canonical_id(workflow.name, workflow.kind)
    for index, step in enumerate(workflow.steps, start=1):
        step_id = canonical_id(step, "Action")
        tx.run(
            """
            MERGE (workflow:OntologyEntity {namespace: $namespace, id: $workflow_id})
            MERGE (step:OntologyEntity {namespace: $namespace, id: $step_id})
            ON CREATE SET step.name = $step_name, step.kind = "Action", step.aliases = [], step.properties_json = "{}"
            SET step:OntologyAction
            MERGE (workflow)-[r:RELATES {namespace: $namespace, rel_type: "HAS_STEP", source_path: $path}]->(step)
            SET r.order = $step_order,
                r.batch_id = $batch_id
            WITH step
            MATCH (b:OntologyBatch {namespace: $namespace, id: $batch_id})
            MERGE (b)-[:MENTIONS]->(step)
            """,
            namespace=NAMESPACE,
            workflow_id=workflow_id,
            step_id=step_id,
            step_name=step,
            step_order=index,
            batch_id=batch_id,
            path=path,
        )


def _merge_action_io(tx: Any, action: ExtractedAction, batch_id: str, path: str) -> None:
    action_id = canonical_id(action.name, action.kind)
    for rel_type, values in {"REQUIRES": action.requires, "PRODUCES": action.produces}.items():
        for value in values:
            target_id = canonical_id(value)
            tx.run(
                """
                MERGE (action:OntologyEntity {namespace: $namespace, id: $action_id})
                MERGE (target:OntologyEntity {namespace: $namespace, id: $target_id})
                ON CREATE SET target.name = $target_name, target.kind = "Thing", target.aliases = [], target.properties_json = "{}"
                MERGE (action)-[r:RELATES {namespace: $namespace, rel_type: $rel_type, source_path: $path}]->(target)
                SET r.batch_id = $batch_id
                WITH target
                MATCH (b:OntologyBatch {namespace: $namespace, id: $batch_id})
                MERGE (b)-[:MENTIONS]->(target)
                """,
                namespace=NAMESPACE,
                action_id=action_id,
                target_id=target_id,
                target_name=value,
                rel_type=rel_type,
                batch_id=batch_id,
                path=path,
            )


def _normalize_rel_type(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").upper()
    return normalized or "RELATED_TO"


def _record_to_dict(record: Any) -> dict[str, Any]:
    node = dict(record["n"])
    node["relationships"] = [
        item for item in record["relationships"]
        if item.get("type") and item.get("neighbor")
    ]
    return node
