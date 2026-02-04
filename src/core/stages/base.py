from abc import ABC, abstractmethod

from core.tasks.base import TaskBase
import logging
logger = logging.getLogger(__name__)

class StageBase(ABC):
    """
    Abstract base class for all stages in the pipeline.

    A stage is a logical grouping of tasks. The `run` method is responsible
    for executing the tasks within the stage.
    """

    name: str
    depends_on: list[str] | None
    tasks: list[TaskBase]

    #@abstractmethod
    def run(self, context: dict) -> dict:
        """
        Runs all tasks within the stage.

        Args:
            context: The current pipeline context.

        Returns:
            The updated pipeline context.
        """
        logger.info(f"--- Starting Stage: {self.name} ---")
        for task in self.tasks:
            logger.info(f"Executing task: {task.name}")
            context = task.execute(context)
        logger.info(f"--- Stage {self.name} Completed ---")
        return context

    @classmethod
    def add_task(cls, task: TaskBase) -> None:
        """
        Adds a task to the stage.

        Args:
            task: The task to add.
        """
        cls.tasks.append(task)