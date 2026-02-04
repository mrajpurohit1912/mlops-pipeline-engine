import json
from pathlib import Path

import yaml

from configuration.config_parser.base import ParserBase


class YamlParser(ParserBase):
    def parse(self, config_path: Path) -> dict:
        try:
            with open(config_path) as f:
                config_content = yaml.safe_load(f)
                # return MLConfig(**config_content)
                return config_content
        except Exception as e:
            raise e


class JsonParser(ParserBase):
    def parse(self, config_path: Path) -> dict:
        try:
            with open(config_path) as f:
                config_content = json.load(f)
                return config_content
        except Exception as e:
            raise e
