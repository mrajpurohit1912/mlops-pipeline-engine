from configuration.schema.base_config_schema import Stage
from configuration.schema.input_config_schema import MLConfig
from core.stages.base import StageBase
from core.stages.stages import DataIngestionStage, DataValidationStage
from execution.data_ingestor.factory import DataIngestorFactory
from execution.data_validation.factory import DataValidatorFactory


class DAGGenerator:
    """
    Generates the pipeline's execution plan as a list of stages (the DAG).
    """

    def generate_execution_plan(
        self, validated_input_config: MLConfig, validated_default_config: Stage
    ) -> list[StageBase]:
        """
        Generates a list of stages based on the pipeline configuration.

        Args:
            config: The validated pipeline configuration.

        Returns:
            A list of `StageBase` objects representing the execution plan.
        """
        stages = []

        for stage_config in validated_default_config.stages:
            if stage_config.enabled and stage_config.stage_name == "data_ingestion":
                ingestion_stage = DataIngestionStage()
                for task in stage_config.tasks:
                    if task.enabled:
                        ingestion_task = DataIngestorFactory.create_task(
                            task.task_name, validated_input_config
                        )
                        ingestion_stage.add_task(ingestion_task)
                stages.append(ingestion_stage)

            elif stage_config.enabled and stage_config.stage_name == "data_validation":
                data_validation_stage = DataValidationStage()
                for task in stage_config.tasks:
                    if task.enabled:
                        validation_task = DataValidatorFactory.create_task(
                            task.task_name, validated_input_config
                        )
                        data_validation_stage.add_task(validation_task)
                stages.append(data_validation_stage)

        return stages
