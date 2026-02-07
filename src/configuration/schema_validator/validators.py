from configuration.schema.base_config_schema import DefaultConfig
from configuration.schema.input_config_schema import MLConfig
from configuration.schema_validator.base import SchemaValidatorBase


class InputSchemaValidator(SchemaValidatorBase):
    def validate(self, raw_config: dict) -> MLConfig:
        return MLConfig(**raw_config)


class DefaultSchemaValidator(SchemaValidatorBase):
    def validate(self, raw_config: dict) -> DefaultConfig:
        return DefaultConfig(**raw_config)
