from configuration.config_parser.base import ParserBase
from configuration.config_parser.parsers import JsonParser, YamlParser


class ConfigParserFactory:
    @staticmethod
    def get_parser(parser_type: str) -> ParserBase:
        if parser_type.lower() == "yaml":
            return YamlParser()
        elif parser_type.lower() == "json":
            return JsonParser()
        else:
            raise ValueError(f"Unsupported config parser type: {parser_type} ")
