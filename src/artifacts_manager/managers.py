from artifacts_manager.base import ArtifactManagerBase
from artifacts_manager.models.models import ArtifactsInput,ArtifactsOutput


class DatasetArtifactManager(ArtifactManagerBase):
    """
    Artifact Manager for managing,versioning the datasets
    """

    def save_artifact(artifact_input:ArtifactsInput)->ArtifactsOutput:
        pass    

    def get_artifact(artifact_id:str)->ArtifactsOutput:
        pass

class ModelArtifactManager(ArtifactManagerBase):
    """
    Artifact Manager for managing,versioning the models
    """

    def save_artifact(artifact_input:ArtifactsInput)->ArtifactsOutput:
        pass    

    def get_artifact(artifact_id:str)->ArtifactsOutput:
        pass