from datetime import datetime
from pathlib import Path

import polars as pl

from artifacts_manager.models.models import ArtifactsInput, ArtifactType
from core.models.metadata import (
    ExecutionStatus,
    PipelineContext,
    TaskExecutionResult,
)
from core.tasks.base import TaskBase


class CsvIngestor(TaskBase):
    """
    A task for ingesting data from a CSV file.
    """

    name = "csv_data_ingestor"

    def __init__(self, data_path: Path):
        self.data_path = data_path

    def execute(self, context: PipelineContext) -> TaskExecutionResult:
        """
        Reads a CSV file into a Polars DataFrame and registers it as an artifact.

        Args:
            context: The pipeline context.

        Returns:
            A TaskExecutionResult with the artifact_id of the registered artifact.
        """
        metadata = self._prepare_metadata(context, self.name)
        try:
            df = pl.read_csv(self.data_path)

            artifact_input = ArtifactsInput(
                stage_name="data_ingestion",
                task_name=self.name,
                artifact_name="raw_dataset",
                artifact_type=ArtifactType.DATASET,
                artifact_path=str(self.data_path),
                pipeline_run_id=context.pipeline_run_id,
                created_at=datetime.now(),
            )
            artifact_output = context.artifact_manager.register_artifact(artifact_input)

            metadata.status = ExecutionStatus.COMPLETED
            metadata.end_at = datetime.utcnow()

            return TaskExecutionResult(
                metadata=metadata,
                output={"row_count": len(df)},
                artifacts={"dataset_id": artifact_output.artifact_id},
            )
        except Exception as e:
            metadata.status = ExecutionStatus.FAILED
            metadata.error_message = str(e)
            metadata.end_at = datetime.utcnow()
            raise e
