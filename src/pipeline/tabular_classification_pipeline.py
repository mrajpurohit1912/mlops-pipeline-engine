# from config import Config
# from orchestrator.orchestrator import PipelineOrchestrator
# from configuration.config_parser.yaml_parser import YamlParser


# class TabularPipeline():
#     def __init__(self,parser,dag,pipeline_orchestrator:PipelineOrchestrator):
#         self.pipeline_orchestrator = pipeline_orchestrator

#     def run(self):
#         self.pipeline_orchestrator.run()

# if __name__ == "__main__":
#     config = Config()
#     yaml_parser = YamlParser(config.CLASSIFICATION_PIPELINE_CONFIG_PATH)
#     main_pipeline = TabularPipeline(PipelineOrchestrator)
#     main_pipeline.run()


from pathlib import Path
from configuration.configuration_engine import ConfigurationEngine
from configuration.models.config_model import MLConfig
from orchestrator.orchestrator import PipelineOrchestrator



class TabularClassificationPipeline:
    def __init__(self,configuration_engine:ConfigurationEngine,orchestrator:PipelineOrchestrator):
        self.configuration_engine = configuration_engine
        self.orchestrator = orchestrator 

    def run(self,config_path:Path):
        complete_plan = self.configuration_engine.build_execution_plan(config_path)

        self.orchestrator.run(complete_plan)
