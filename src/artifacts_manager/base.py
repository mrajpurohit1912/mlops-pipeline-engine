from abc import ABC, abstractmethod

from artifacts_manager.models.models import ArtifactsInput,ArtifactsOutput




class ArtifactManagerBase(ABC):
    """
    Base Class for artifact manager.
    """


    @abstractmethod
    def save_artifact(artifact_input:ArtifactsInput)->ArtifactsOutput:
        pass

    @abstractmethod
    def get_artifact(artifact_id:str)->ArtifactsOutput:
        pass