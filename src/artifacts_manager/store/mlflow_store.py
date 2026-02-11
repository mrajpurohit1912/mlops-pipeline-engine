import mlflow

from artifacts_manager.models.models import ArtifactsOutput


class MLflowStore:
    """
    An MLflow store for saving artifact metadata.
    """

    def __init__(self, tracking_uri: str):
        mlflow.set_tracking_uri(tracking_uri)

    def save_artifact(self, artifact: ArtifactsOutput) -> None:
        """
        Saves the artifact metadata to the MLflow tracking server.

        Args:
            artifact: An instance of ArtifactsOutput containing artifact details.
        """
        with mlflow.start_run(run_id=artifact.pipeline_run_id):
            mlflow.log_dict(artifact.dict(), "artifact_metadata.json")

    def get_artifact(self, artifact_id: str) -> ArtifactsOutput | None:
        """
        Retrieves the artifact metadata from the MLflow tracking server.

        Args:
            artifact_id: The unique identifier of the artifact to retrieve.
        Returns:
            An instance of ArtifactsOutput containing the retrieved artifact details,
            or None if the artifact is not found.
        """
        # In MLflow, artifacts are associated with runs. To get an artifact,
        # we need to know the run_id. This implementation assumes that the
        # artifact_id is the run_id.
        try:
            artifact_path = mlflow.get_artifact_uri("artifact_metadata.json")
            with open(artifact_path) as f:
                import json

                artifact_data = json.load(f)
            return ArtifactsOutput(**artifact_data)
        except Exception:
            return None
