from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class ExecutionStatus(str, Enum):
    """
    Status of the execution
    """

    PENDING: str = "PENDING"
    RUNNING: str = "RUNNING"
    COMPLETED: str = "COMPLETED"
    FAILED: str = "FAILED"


class BaseMetaData(BaseModel):
    """
    Base Metadata model for tracking and maintaining the execution status
    """

    id: str = Field(default_factory=lambda: str(uuid4()))
    pipeline_run_id: str
    name: str
    status: ExecutionStatus = ExecutionStatus.PENDING
    started_at: datetime | None = None
    end_at: datetime | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    error_message: str | None = None


class TaskExecutionResult(BaseModel):
    """
    Model for tracking the execution result of a task or stage
    """

    metadata: BaseMetaData
    output: dict[str, Any] | None = None
    artifacts: dict[str, str] | None = None


class StageExecutionResult(BaseModel):
    metadata = BaseMetaData
    task_results = dict[str, TaskExecutionResult]


class PipelineExecutionResult(BaseModel):
    pipeline_run_id: str
    stages: dict[str, StageExecutionResult]


class PipelineContext(BaseModel):
    pipeline_run_id: str
    stage_results: dict[str, StageExecutionResult] = {}
    task_results: dict[str, TaskExecutionResult] = {}
