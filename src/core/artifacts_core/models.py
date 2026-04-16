from datetime import datetime
from enum import Enum

from pydantic import BaseModel
from typing import Literal
from pathlib import Path



class ArtifactType(str, Enum):
    DATASET = "dataset"
    MODEL = "model"
    METRICS = "metrics"
    REPORT = "report"


class ArtifactsInput(BaseModel):
    stage_name: str
    task_name: str
    # artifact_id:str
    artifact_name: str
    artifact_type: ArtifactType
    artifact_path: str
    # version:str
    pipeline_run_id: str
    created_at: datetime
    metadata: dict | None = None


class ArtifactsOutput(BaseModel):
    stage_name: str
    task_name: str
    artifact_id: str
    artifact_name: str
    artifact_type: ArtifactType
    artifact_path: str
    version: str
    pipeline_run_id: str
    created_at: datetime
    metadata: dict | None = None


class ArtifactDescriptor(BaseModel):
    artifact_type: Literal["dataset", "model", "metrics"]
    name: str
    uri: Path
    stage_name: str
    task_name: str
    pipeline_run_id: str
    created_at: datetime

    class Config:
        frozen = True