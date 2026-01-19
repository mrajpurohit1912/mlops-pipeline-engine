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

from core.task_base import TaskBase
from configuration.config_parser.base import ParserBase
from configuration.schema_validator.validator import SchemaValidator
from configuration.dag.dag_generator import DAGGenerator

class ConfigurationEngine:
    def __init__(self,parser:ParserBase,validator:SchemaValidator,dag_generator:DAGGenerator):
        self.parser = parser
        self.validator = validator
        self.dag_generator = dag_generator


    def build_execution_plan(self,config_path:Path)->list[TaskBase]:
        raw = self.parser.parse(config_path)
        validated = self.validator.validate(raw)
        return self.dag_generator.generate(validated)

        