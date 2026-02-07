from pathlib import Path
from datetime import datetime
import polars as pl

from core.tasks.base import TaskBase
from core.models.metadata import (
    BaseMetaData,
    TaskExecutionResult,
    ExecutionStatus,
    PipelineContext,
)




class CsvIngestor(TaskBase):
    """
    A task for ingesting data from a CSV file.
    """

    name = "csv_data_ingestor"

    def __init__(self, data_path: Path):
        self.data_path = data_path

    def execute(self, context:PipelineContext) -> TaskExecutionResult:
        """
        Reads a CSV file into a Polars DataFrame .

        Args:
            pipeline_run_id: Pipeline Run ID.

        Returns:
            ExecutionResult Which is combination of meatadata and the result of the task.
        """
        metadata = self._prepare_metadata(
            context.pipeline_run_id,
            name=self.name,
            )
        
        try:
            df = pl.read_csv(self.data_path)

            metadata.status = ExecutionStatus.COMPLETED
            metadata.end_at = datetime.utcnow()

            return TaskExecutionResult(
                metadata=metadata,
                output={"row_count": len(df)},
                artifacts={"file_path": str(self.data_path)},
                )
        except Exception as e:
            metadata.status = ExecutionStatus.FAILED
            metadata.error_message = str(e)
            metadata.end_at = datetime.utcnow()
            raise e

