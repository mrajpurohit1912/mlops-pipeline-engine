from pydantic import BaseModel,Field
from typing import Literal
from datetime import date

class DatasetSaveRequest(BaseModel):
    dataset_layer: Literal["raw","processed","final"]
    dataset_name:str
    execution_date:date
    pipeline_run_id:str
    version:str = Field(default="1.0")

    format: Literal["parquet","csv"] = Field(default="parquet")

    class Config:
        frozen = True