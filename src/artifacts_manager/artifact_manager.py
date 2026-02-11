from datetime import datetime
from uuid import uuid4

from artifacts_manager.base import ArtifactManagerBase
from artifacts_manager.models.models import ArtifactsInput, ArtifactsOutput
from artifacts_manager.store.local_store import LocalStore
from artifacts_manager.store.mlflow_store import MLflowStore


class ArtifactManager(ArtifactManagerBase):
    """
    Artifact Manager for managing,versioning the datasets
    """

    def __init__(self, store_type: str = "mlflow", tracking_uri: str = "artifacts"):
        if store_type == "local":
            self.store = LocalStore(tracking_uri)
        elif store_type == "mlflow":
            self.store = MLflowStore(tracking_uri)
        else:
            raise ValueError(f"Unsupported store type: {store_type}")

    def register_artifact(self, artifact_input: ArtifactsInput) -> ArtifactsOutput:
        artifact_output = ArtifactsOutput(
            stage_name=artifact_input.stage_name,
            task_name=artifact_input.task_name,
            artifact_id=str(uuid4()),
            artifact_name=artifact_input.artifact_name,
            artifact_type=artifact_input.artifact_type,
            artifact_path=artifact_input.artifact_path,
            version="1.0",
            pipeline_run_id=artifact_input.pipeline_run_id,
            created_at=datetime.now(),
            metadata=artifact_input.metadata,
        )
        self.store.save_artifact(artifact_output)
        return artifact_output

    def get_artifact(self, artifact_id: str) -> ArtifactsOutput:
        return self.store.get_artifact(artifact_id)
