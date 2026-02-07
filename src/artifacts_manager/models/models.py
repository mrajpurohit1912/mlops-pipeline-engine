from pydantic import BaseModel
from enum import Enum

from datetime import datetime



class ArtifactType(str,Enum):
    DATASET = "dataset"
    MODEL = "model"
    METRICS = "metrics"
    REPORT = "report"
    CONFIG = "config"
    PREDICTIONS = "predictions"

class ArtifactsInput(BaseModel):
    stage_name:str
    task_name:str
    artifact_id:str
    artifact_name:str
    artifact_type:ArtifactType
    artifact_path:str
    version:str
    pipeline_run_id:str
    created_at:datetime
    metadata:dict | None=None


class ArtifactsOutput(BaseModel):
    stage_name:str
    task_name:str
    artifact_id:str
    artifact_name:str
    artifact_type:ArtifactType
    artifact_path:str
    version:str
    pipeline_run_id:str
    created_at:datetime
    metadata:dict | None=None




    