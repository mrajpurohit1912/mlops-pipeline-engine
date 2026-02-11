import json
import logging
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

logger = logging.getLogger(__name__)


class MissingValueValidator(TaskBase):
    """
    A task to validate the percentage of missing values in a DataFrame.
    """

    name = "missing_value_validator"

    def __init__(self, missing_percentage: float):
        self.missing_percentage = missing_percentage

    def execute(self, context: PipelineContext) -> TaskExecutionResult:
        """
        Validates that the percentage of missing values in each column does
        not exceed the configured threshold.

        Args:
            context: The current pipeline context.

        Returns:
            A TaskExecutionResult with the artifact_id of the validation report.
        """
        metadata = self._prepare_metadata(context, self.name)
        validation_report = {
            "validation_type": "missing_value_validation",
            "results": {},
        }
        try:
            # Get the dataset artifact from the previous task
            ingestion_task_result = context.task_results["csv_data_ingestor"]
            dataset_id = ingestion_task_result.artifacts["dataset_id"]
            dataset_artifact = context.artifact_manager.get_artifact(dataset_id)
            df = pl.read_csv(dataset_artifact.artifact_path)

            logger.info(
                f"Validating missing values with threshold: {self.missing_percentage}%"
            )
            for col in df.columns:
                missing_count = df[col].is_null().sum()
                total_count = len(df)
                missing_percent = (missing_count / total_count) * 100
                validation_report["results"][col] = {
                    "missing_count": missing_count,
                    "total_count": total_count,
                    "missing_percent": missing_percent,
                }
                if missing_percent > self.missing_percentage:
                    raise ValueError(
                        f"Column '{col}' has {missing_percent:.2f}% missing values, "
                        f"which exceeds the threshold of {self.missing_percentage}%."
                    )
            logger.info("Missing value validation passed.")

            # Save the validation report
            report_path = Path("artifacts") / f"{self.name}_report.json"
            report_path.parent.mkdir(parents=True, exist_ok=True)
            with open(report_path, "w") as f:
                json.dump(validation_report, f, indent=4)

            # Register the validation report as an artifact
            artifact_input = ArtifactsInput(
                stage_name="data_validation",
                task_name=self.name,
                artifact_name="missing_value_validation_report",
                artifact_type=ArtifactType.REPORT,
                artifact_path=str(report_path),
                pipeline_run_id=context.pipeline_run_id,
                created_at=datetime.now(),
            )
            artifact_output = context.artifact_manager.register_artifact(artifact_input)

            metadata.status = ExecutionStatus.COMPLETED
            metadata.end_at = datetime.utcnow()

            return TaskExecutionResult(
                metadata=metadata,
                artifacts={"validation_report_id": artifact_output.artifact_id},
            )
        except Exception as e:
            metadata.status = ExecutionStatus.FAILED
            metadata.error_message = str(e)
            metadata.end_at = datetime.utcnow()
            raise e


class DataTypeValidator(TaskBase):
    """
    A task to validate the data types of columns in a DataFrame.
    """

    name = "data_type_validator"

    def __init__(self, column_config: dict):
        self.column_config = column_config

    def execute(self, context: PipelineContext) -> TaskExecutionResult:
        """
        Validates that the data types of columns match the configured types.

        Args:
            context: The current pipeline context.

        Returns:
            A TaskExecutionResult with the artifact_id of the validation report.
        """
        metadata = self._prepare_metadata(context, self.name)
        validation_report = {"validation_type": "data_type_validation", "results": {}}
        try:
            # Get the dataset artifact from the previous task
            ingestion_task_result = context.task_results["csv_data_ingestor"]
            dataset_id = ingestion_task_result.artifacts["dataset_id"]
            dataset_artifact = context.artifact_manager.get_artifact(dataset_id)
            df = pl.read_csv(dataset_artifact.artifact_path)

            logger.info("Validating column data types.")
            for col_name, expected_type_str in self.column_config.items():
                if col_name not in df.columns:
                    logger.warning(
                        f"Column '{col_name}' from config not found in DataFrame. Skipping."
                    )
                    continue

                actual_type = df[col_name].dtype
                validation_report["results"][col_name] = {
                    "actual_type": str(actual_type),
                    "expected_type": expected_type_str,
                }
                # This mapping is basic; a more robust solution would be needed for production
                type_mapping = {
                    "int": [pl.Int64, pl.Int32, pl.Int16, pl.Int8],
                    "float": [pl.Float64, pl.Float32],
                    "str": [pl.Utf8],
                }
                expected_types = type_mapping.get(expected_type_str)
                if not expected_types or actual_type not in expected_types:
                    raise TypeError(
                        f"Column '{col_name}' has type {actual_type}, but expected "
                        f"type {expected_type_str}."
                    )
            logger.info("Data type validation passed.")

            # Save the validation report
            report_path = Path("artifacts") / f"{self.name}_report.json"
            report_path.parent.mkdir(parents=True, exist_ok=True)
            with open(report_path, "w") as f:
                json.dump(validation_report, f, indent=4)

            # Register the validation report as an artifact
            artifact_input = ArtifactsInput(
                stage_name="data_validation",
                task_name=self.name,
                artifact_name="data_type_validation_report",
                artifact_type=ArtifactType.REPORT,
                artifact_path=str(report_path),
                pipeline_run_id=context.pipeline_run_id,
                created_at=datetime.now(),
            )
            artifact_output = context.artifact_manager.register_artifact(artifact_input)

            metadata.status = ExecutionStatus.COMPLETED
            metadata.end_at = datetime.utcnow()

            return TaskExecutionResult(
                metadata=metadata,
                artifacts={"validation_report_id": artifact_output.artifact_id},
            )
        except Exception as e:
            metadata.status = ExecutionStatus.FAILED
            metadata.error_message = str(e)
            metadata.end_at = datetime.utcnow()
            raise e
