import yaml
from pathlib import Path
from  configuration.config_parser.base import ParserBase
from configuration.models.config_model import MLConfig


class YamlParser(ParserBase):
    def parse(self,config_path:Path)->MLConfig:
        try:
            with open(config_path,'r') as f:
                config_content = yaml.safe_load(f)
            # return MLConfig(**config_content)
                return config_content
        except Exception as e:
            raise e
