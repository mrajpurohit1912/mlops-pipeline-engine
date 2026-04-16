from configuration.schema.input_config_schema import DataConfig
from core.tasks.base import TaskBase
from application.tasks.data_ingestor import CsvIngestor


class DataIngestorFactory:
    """
    Factory for creating data ingestion tasks.
    """

    @staticmethod
    def create_task(task_name: str, input_source_config: DataConfig) -> TaskBase:
        """
        Creates a data ingestion task based on the source configuration.

        Args:
            task_name: The name of the task to create.
            input_source_config: The data source configuration object.

        Returns:
            An instance of a configured data ingestion task.
        """
        if task_name == "csv_data_ingestor":
            return CsvIngestor(data_path=input_source_config.data.path)
        else:
            raise ValueError(f"Unsupported ingestor type: {task_name}")
