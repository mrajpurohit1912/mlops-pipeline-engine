# from config import Config
# from configuration.config_parser.yaml_parser import YamlParser
# from configuration.dag.dag_generator import DAG

# class ConfigurationMain:
#     def __init__(self,yaml_parser:YamlParser,dag:DAG):
#         self.yaml_parser = yaml_parser
#         self.dag = dag

#     def run(self):
#         self.ml_config_output = self.yaml_parser.parse()
#         self.dag_plan = self.dag(self.ml_config_output)
#         return self.dag_plan


# if __name__ == "__main__":
#     config = Config()
#     yaml_parser = YamlParser(config.CLASSIFICATION_PIPELINE_CONFIG_PATH)
#     DAG

#     config_main = ConfigurationMain()

from pathlib import Path

from configuration.config_parser.base import ParserBase
from configuration.dag.dag_generator import DAGGenerator
from configuration.schema_validator.validators import SchemaValidatorBase
from core.stages.base import StageBase


class ConfigurationEngine:
    def __init__(
        self,
        input_config_parser: ParserBase,
        default_config_parser: ParserBase,
        input_validator: SchemaValidatorBase,
        default_validator: SchemaValidatorBase,
        dag_generator: DAGGenerator,
    ):
        self.input_config_parser = input_config_parser
        self.default_config_parser = default_config_parser
        self.input_validator = input_validator
        self.default_validator = default_validator
        self.dag_generator = dag_generator

    def build_execution_plan(self, input_config_path: Path,default_config_path: Path
) -> list[StageBase]:
        raw_input_config = self.input_config_parser.parse(input_config_path)
        raw_default_config = self.default_config_parser.parse(default_config_path)
        validated_input_config = self.input_validator.validate(raw_input_config)
        validated_default_config = self.default_validator.validate(raw_default_config)
        return self.dag_generator.generate_execution_plan(validated_input_config, validated_default_config)