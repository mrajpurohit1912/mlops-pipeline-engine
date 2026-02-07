from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class StageMetaData(BaseModel):
    pipeline_run_id: str
    task_name: str
    status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED"]
    created_at: datetime = datetime.now()
    error_message: str | None = None


class StageResult(BaseModel):
    artifacts: dict[str, str]
    metrics: dict[str, float] | None = None


class StageExecutionResult(BaseModel):
    metadata: StageMetaData
    result: StageResult
