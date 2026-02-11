from pathlib import Path
from uuid import uuid4

from configuration.configuration_engine import ConfigurationEngine
from orchestrator.orchestrator import PipelineOrchestrator


class TabularClassificationPipeline:
    def __init__(
        self,
        configuration_engine: ConfigurationEngine,
        orchestrator: PipelineOrchestrator,
    ):
        self.configuration_engine = configuration_engine
        self.orchestrator = orchestrator

    def run(
        self,
        input_config_path: Path,
        default_config_path: Path,
    ):
        complete_plan = self.configuration_engine.build_execution_plan(
            input_config_path,
            default_config_path,
        )

        context_result = self.orchestrator.run(
            stages=complete_plan,
            pipeline_run_id=str(uuid4()),
        )
        return context_result
