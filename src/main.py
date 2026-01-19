from config import Config
from pipeline.tabular_classification_pipeline import TabularClassificationPipeline
from configuration.configuration_engine import ConfigurationEngine
from configuration.config_parser.yaml_parser import YamlParser
from configuration.schema_validator.validator import SchemaValidator
from configuration.dag.dag_generator import DAGGenerator
from orchestrator.orchestrator import PipelineOrchestrator

def main():
    config = Config()
    yaml_parser = YamlParser()
    schema_validator = SchemaValidator()
    dag_generator = DAGGenerator()

    configuration_engine = ConfigurationEngine(yaml_parser,schema_validator,dag_generator)

    orchestrator = PipelineOrchestrator()
    tabular_classification_pipeline = TabularClassificationPipeline(configuration_engine,orchestrator)

    tabular_classification_pipeline.run(config.CLASSIFICATION_PIPELINE_CONFIG_PATH)


if __name__ == "__main__":
    main()