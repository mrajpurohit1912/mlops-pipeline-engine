import logging

from artifacts_manager.artifact_manager import ArtifactManager
from core.models.metadata import (
    PipelineContext,
    PipelineExecutionResult,
)
from core.stages.base import StageBase

logger = logging.getLogger(__name__)


class PipelineOrchestrator:
    """
    Orchestrates the execution of a pipeline by running a list of stages.
    """

    def __init__(self, artifact_manager: ArtifactManager):
        self.artifact_manager = artifact_manager

    def run(
        self, stages: list[StageBase], pipeline_run_id: str
    ) -> PipelineExecutionResult:
        """
        Executes a pipeline by running its stages in sequence.

        Args:
            stages: A list of `StageBase` objects representing the pipeline's
                    execution plan.

        Returns:
            The final context dictionary after all stages have been executed.
        """
        logger.info("Starting pipeline execution.")
        stage_results = {}

        context = PipelineContext(
            pipeline_run_id=pipeline_run_id,
            artifact_manager=self.artifact_manager,
        )

        for stage in stages:
            result = stage.run(context)
            stage_results[stage.name] = result

        return PipelineExecutionResult(
            pipeline_run_id=pipeline_run_id,
            stages=stage_results,
        )

    # def stage_manager(self,result):#result has to be the metadata + result of task/stage
    #     """
    #     Checks the status of the stage/task and update in Metadata Store.

    #     Args:
    #         result: The result of the stage/task
    #     Return:
    #         None
    #     """

    #     if result.status == "SUCCESS":# Complete the logic here
    #         pass
    #     else:
    #         pass
