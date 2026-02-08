# import argparse
# from pathlib import Path


# from configuration.config_parser.factory import ConfigParserFactory
# from configuration.configuration_engine import ConfigurationEngine
# from configuration.dag.dag_generator import DAGGenerator
# from configuration.schema_validator.factory import SchemaValidatorFactory
# from orchestrator.orchestrator import PipelineOrchestrator
# from pipeline.tabular_classification_pipeline import TabularClassificationPipeline
from app_config import Config
from runtime.bootstrap import RuntimeBootstrapper


def main():
    config = Config()
    RuntimeBootstrapper(config).bootstrap()

    # parser = argparse.ArgumentParser()
    # parser.add_argument("config_path", type=Path)
    # parser.add_argument("default_config_path", type=Path)
    # args = parser.parse_args()

    # input_config_parser = ConfigParserFactory.get_parser(
    #     args.config_path.suffix.lstrip(".")
    # )
    # default_config_parser = ConfigParserFactory.get_parser(
    #     args.default_config_path.suffix.lstrip(".")
    # )

    # input_schema_validator = SchemaValidatorFactory.get_schema_validator(
    #     args.config_path
    # )
    # default_schema_validator = SchemaValidatorFactory.get_schema_validator(
    #     args.default_config_path
    # )

    # dag_generator = DAGGenerator()

    # configuration_engine = ConfigurationEngine(
    #     input_config_parser,
    #     default_config_parser,
    #     input_schema_validator,
    #     default_schema_validator,
    #     dag_generator,
    # )

    # orchestrator = PipelineOrchestrator()
    # tabular_classification_pipeline = TabularClassificationPipeline(
    #     configuration_engine, orchestrator
    # )

    # context_result = tabular_classification_pipeline.run(
    #     args.config_path, args.default_config_path
    # )

    # print(f"Context result: {context_result}")


if __name__ == "__main__":
    main()
