from datetime import date,datetime
from pathlib import Path

import polars as pl

from core.artifacts_core.models import ArtifactsInput, ArtifactType
from core.models.metadata import (
    ExecutionStatus,
    PipelineContext,
    TaskExecutionResult,
)
from core.tasks.base import TaskBase
from utils.dataset_manager.dto import DatasetSaveRequest



class CsvIngestor(TaskBase):
    """
    A task for ingesting data from a CSV file.
    """

    name = "csv_data_ingestor"

    def __init__(self, data_path: Path):
        self.data_path = data_path

    def _read_csv(self) -> pl.DataFrame:
        """
        Reads a CSV file into a Polars DataFrame.

        Returns:
            A Polars DataFrame containing the data from the CSV file.
        """
        return pl.read_csv(self.data_path)



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
            df = self._read_csv()

            save_request = DatasetSaveRequest(
            dataset_layer="raw",
            dataset_name="raw_dataset",
            execution_date=date.today(),
            pipeline_run_id=context.pipeline_run_id,
            version="1.0",
            )

            dataset_path = context.dataset_manager.save_dataset(
            dataset=df,
            request=save_request,
            )

            metadata.status = ExecutionStatus.COMPLETED
            metadata.end_at = datetime.utcnow()

            return TaskExecutionResult(
                metadata=metadata,
                output={"dataset_path": dataset_path},
            )
        except Exception as e:
            metadata.status = ExecutionStatus.FAILED
            metadata.error_message = str(e)
            metadata.end_at = datetime.utcnow()
            raise e
