from abc import ABC, abstractmethod


class TaskBase(ABC):
    """
    Abstract base class for all tasks in the pipeline.

    Each task must implement the `execute` method, which takes the current
    pipeline context and returns the updated context.
    """

    name: str
    depends_on: list[str] | None = None

    @abstractmethod
    def execute(self, context: dict) -> dict:
        """
        Executes the task.

        Args:
            context: A dictionary representing the current state of the pipeline.

        Returns:
            The updated context dictionary.
        """
        pass

