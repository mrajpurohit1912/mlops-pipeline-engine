import logging
import uuid
from core.stages.base import StageBase

logger = logging.getLogger(__name__)


class PipelineOrchestrator:
    """
    Orchestrates the execution of a pipeline by running a list of stages.
    """

    def run(self, stages: list[StageBase]) -> dict:
        """
        Executes a pipeline by running its stages in sequence.

        Args:
            stages: A list of `StageBase` objects representing the pipeline's
                    execution plan.

        Returns:
            The final context dictionary after all stages have been executed.
        """
        #run_id = str(uuid.uuid4())
        # The logger adapter is configured in main.py, but we can add the run_id here.
        # A better solution would be to use a centralized context object.
        #log_adapter = logging.LoggerAdapter(logger, {"run_id": run_id})

        #log_adapter.info("--- Starting Pipeline Execution ---")
        #context = {"run_id": run_id}
        context = {}

        for stage in stages:
            context = stage.run(context)
            #log_adapter.info(f"Context: {context}")

        #log_adapter.info("--- Pipeline Execution Completed ---")
        return context
