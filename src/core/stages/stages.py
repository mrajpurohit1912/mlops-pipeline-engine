import logging

from core.stages.base import StageBase
from core.tasks.base import TaskBase

logger = logging.getLogger(__name__)


class DataIngestionStage(StageBase):
    """
    A pipeline stage for ingesting data.
    """

    name = "data_ingestion_stage"
    depends_on = None
    tasks = []

    # def __init__(self, task: TaskBase):
    #     self.tasks = [task]

    # def run(self, context: dict) -> dict:
    #     """
    #     Runs the data ingestion task.

    #     Args:
    #         context: The current pipeline context.

    #     Returns:
    #         The updated context with the ingested DataFrame.
    #     """
    #     logger.info(f"--- Starting Stage: {self.name} ---")
    #     for task in self.list_of_tasks:
    #         logger.info(f"Executing task: {task.name}")
    #         context = task.execute(context)
    #     logger.info(f"--- Stage {self.name} Completed ---")
    #     return context

    # @classmethod
    # def add_task(cls, task: TaskBase) -> None:
    #     """
    #     Adds a task to the stage.

    #     Args:
    #         task: The task to add.
    #     """
    #     cls.list_of_tasks.append(task)


class DataValidationStage(StageBase):
    """
    A pipeline stage for validating data.
    """

    name = "data_validation_stage"
    depends_on = ["data_ingestion_stage"]
    tasks = []

    # def __init__(self, tasks: list[TaskBase]):
    #     self.list_of_tasks = tasks

    # def run(self, context: dict) -> dict:
    #     """
    #     Runs the data validation tasks.

    #     Args:
    #         context: The current pipeline context.

    #     Returns:
    #         The context, unchanged if validation is successful.
    #     """
    #     logger.info(f"--- Starting Stage: {self.name} ---")
    #     for task in self.list_of_tasks:
    #         logger.info(f"Executing task: {task.name}")
    #         context = task.execute(context)
    #     logger.info(f"--- Stage {self.name} Completed ---")
    #     return context
