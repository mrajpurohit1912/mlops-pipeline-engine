from pathlib import Path

import polars as pl
from core.tasks.base import TaskBase


class CsvIngestor(TaskBase):
    """
    A task for ingesting data from a CSV file.
    """

    name = "csv_data_ingestor"

    def __init__(self, data_path: Path):
        self.data_path = data_path

    def execute(self, context: dict) -> dict:
        """
        Reads a CSV file into a Polars DataFrame and adds it to the context.

        Args:
            context: The current pipeline context.

        Returns:
            The updated context with the DataFrame.
        """
        df = pl.read_csv(self.data_path)
        context["df"] = df
        return context