from pathlib import Path

from configuration.schema_validator.base import SchemaValidatorBase
from configuration.schema_validator.validators import DefaultSchemaValidator, InputSchemaValidator    

class SchemaValidatorFactory:
    
    def get_schema_validator(config_path:Path)->SchemaValidatorBase:
        if "base" in config_path.stem:
            return DefaultSchemaValidator()
        else:
            return InputSchemaValidator()