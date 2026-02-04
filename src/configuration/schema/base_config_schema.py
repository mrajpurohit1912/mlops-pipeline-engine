from pydantic import BaseModel,Field
from typing import Any,Literal
from enum import Enum

class TaskNames(str,Enum):
    csv_data_ingestor: str = "csv_data_ingestor"
    missing_value_validator: str = "missing_value_validator"
    data_type_validator: str = "data_type_validator"


class Task(BaseModel):
    enabled: bool = True
    task_name: TaskNames
    params: dict = {}


class Stage(BaseModel):
    enabled: bool = Field(default=True)
    stage_name: Literal[
        "data_ingestion",
        "data_validation",
        "data_cleaning",
        "feature_engineering",
        "model_training",
    ]
    tasks: list[Task] = Field(default_factory=list)

    
class DefaultConfig(BaseModel):
    stages: list[Stage]

