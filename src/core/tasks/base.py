import uuid
from abc import ABC, abstractmethod
from datetime import datetime

from core.models.metadata import (
    BaseMetaData,
    ExecutionStatus,
    PipelineContext,
    TaskExecutionResult,
)


class TaskBase(ABC):
    """
    Abstract base class for all tasks in the pipeline.

    Each task must implement the `execute` method, which takes the current
    pipeline context and returns the updated context.
    """

    name: str
    depends_on: list[str] | None = None

    def __init__(self):
        self.task_id: str = str(uuid.uuid4())

    def _prepare_metadata(
        self, context: PipelineContext, task_name: str
    ) -> BaseMetaData:
        return BaseMetaData(
            pipeline_run_id=context.pipeline_run_id,
            name=task_name,
            status=ExecutionStatus.RUNNING,
            started_at=datetime.utcnow(),
        )

    @abstractmethod
    def execute(
        self, context: PipelineContext, pipeline_id: str
    ) -> TaskExecutionResult:
        """
        Executes the task.

        Args:
            context: A dictionary representing the current state of the pipeline.

        Returns:
            The updated context dictionary.
        """
        pass
