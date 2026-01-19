from pydantic import BaseModel,Field
from typing import Literal,Dict
from pathlib import Path

class PipelineConfig(BaseModel):
    name:str
    type:Literal["tabular_regression_pipeline","tabular_classification_pipeline","nlp_pipeline"]

class DataSourceConfig(BaseModel):
    name:str
    type:Literal["csv","xlsx"]
    path:Path

class FeaturesConfig(BaseModel):
    include: Literal["all",None]
    feature_config_path:Path
    target:str

class DataConfig(BaseModel):
    source:DataSourceConfig
    features:FeaturesConfig

class ColumnTypeConfig(BaseModel):
    name:str
    dtype:Literal["int", "float", "str", "bool"]

class DataTypeValidationConfig(BaseModel):
    columns: Dict[str,ColumnTypeConfig]


class ValidationConfig(BaseModel):
    enabled:bool = True
    missing_value_validation_percent:int = Field(ge=0,le=100,description="Allowed Missing Value Percentage")
    data_type_validation:DataTypeValidationConfig

class MLConfig(BaseModel):
    pipeline: PipelineConfig
    environment: Literal["dev", "stage", "prod"]
    data: DataConfig
    validation: ValidationConfig
