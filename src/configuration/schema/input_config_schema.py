from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field


class DataConfig(BaseModel):
    name: str
    type: Literal["csv", "xlsx"]
    path: Path
    include: Literal["all", None]
    target_column: str


class ColumnTypeConfig(BaseModel):
    name: str
    dtype: Literal["int", "float", "str", "bool"]


class DataTypeValidationConfig(BaseModel):
    columns: dict[str, ColumnTypeConfig]


class MissingValueValidationConfig(BaseModel):
    missing_percentage: float = Field(
        ge=0, le=100, description="Allowed Missing Value Percentage"
    )

class DataValidationConfig(BaseModel):
    missing_value_validation: MissingValueValidationConfig
    data_type_validation: DataTypeValidationConfig


class MLConfig(BaseModel):
    environment: Literal["dev", "stage", "prod"]
    data: DataConfig
    data_validation: DataValidationConfig
