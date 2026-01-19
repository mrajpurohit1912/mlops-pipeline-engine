from configuration.models.config_model import MLConfig

class SchemaValidator:
    def validate(self,raw_config:dict)->MLConfig:
        return MLConfig(**raw_config)