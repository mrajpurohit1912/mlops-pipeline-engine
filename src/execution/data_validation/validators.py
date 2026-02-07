import logging

import polars as pl

from core.tasks.base import TaskBase
from core.models.metadata import TaskExecutionResult


logger = logging.getLogger(__name__)


class MissingValueValidator(TaskBase):
    """
    A task to validate the percentage of missing values in a DataFrame.
    """

    name = "missing_value_validator"

    def __init__(self, missing_percentage: float):
        self.missing_percentage = missing_percentage

    def execute(self) -> TaskExecutionResult:
        """
        Validates that the percentage of missing values in each column does
        not exceed the configured threshold.

        Args:
            context: The current pipeline context, containing the DataFrame 'df'.

        Returns:
            The context, unchanged.

        Raises:
            ValueError: If any column's missing value percentage exceeds the threshold.
        """
        df = context["df"]
        logger.info(
            f"Validating missing values with threshold: {self.missing_percentage}%"
        )
        for col in df.columns:
            missing_count = df[col].is_null().sum()
            total_count = len(df)
            missing_percent = (missing_count / total_count) * 100
            if missing_percent > self.missing_percentage:
                raise ValueError(
                    f"Column '{col}' has {missing_percent:.2f}% missing values, "
                    f"which exceeds the threshold of {self.missing_percentage}%."
                )
        logger.info("Missing value validation passed.")
        return context


class DataTypeValidator(TaskBase):
    """
    A task to validate the data types of columns in a DataFrame.
    """

    name = "data_type_validator"

    def __init__(self, column_config: dict):
        self.column_config = column_config

    def execute(self) -> TaskExecutionResult:
        """
        Validates that the data types of columns match the configured types.

        Args:
            context: The current pipeline context, containing the DataFrame 'df'.

        Returns:
            The context, unchanged.

        Raises:
            TypeError: If any column's data type does not match the configured type.
        """
        df = context["df"]
        logger.info("Validating column data types.")
        for col_name, expected_type_str in self.column_config.items():
            if col_name not in df.columns:
                logger.warning(
                    f"Column '{col_name}' from config not found in DataFrame. Skipping."
                )
                continue

            actual_type = df[col_name].dtype
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
        return context
