import logging
import uuid
from abc import ABC
from datetime import datetime

from core.models.metadata import (
    BaseMetaData,
    ExecutionStatus,
    StageExecutionResult,
    TaskExecutionResult,
    PipelineContext
)
from core.tasks.base import TaskBase

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

    def __init__(self):
        self.stage_id: str = str(uuid.uuid4())

    def _prepare_metadata(
        self,
        pipeline_run_id: str,
    ) -> BaseMetaData:
        return BaseMetaData(
            pipeline_run_id=pipeline_run_id,
            name=self.name,
            status=ExecutionStatus.RUNNING,
            started_at=datetime.utcnow(),
        )

    def run(
        self,
        context: PipelineContext,
    ) -> StageExecutionResult:
        """
        Runs all tasks within the stage.

        Args:
            context: The current pipeline context.

        Returns:
            The updated pipeline context.
        """
        logger.info(f"--- Starting Stage: {self.name} ---")
        stage_metadata = self._prepare_metadata(
            pipeline_run_id=context.pipeline_run_id, 
        )

        task_results: dict[str, TaskExecutionResult] = {}

        try:
            for task in self.tasks:
                logger.info(f"Executing task: {task.name}")
                result = task.execute(context)
                context.task_results[task.name] = result
                task_results[task.name] = result
                logger.info(
                    f"Task {task.name} executed successfully. with task status {result.metadata.status}"
                )

            stage_metadata.status = ExecutionStatus.COMPLETED
            logger.info(
                f"--- Stage {self.name} Completed  with status {stage_metadata.status} ---"
            )
        except Exception as e:
            stage_metadata.status = ExecutionStatus.FAILED
            stage_metadata.error_message = str(e)
            raise
        finally:
            stage_metadata.end_at = datetime.utcnow()
        return StageExecutionResult(
            metadata=stage_metadata,
            task_results=task_results,
        )

    @classmethod
    def add_task(cls, task: TaskBase) -> bool:
        """
        Adds a task to the stage.

        Args:
            task: The task to add.
        """
        cls.tasks.append(task)
