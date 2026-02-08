from abc import ABC, abstractmethod

from artifacts_manager.models.models import ArtifactsInput, ArtifactsOutput


class ArtifactManagerBase(ABC):
    """
    Base Class for artifact manager.
    """

    @abstractmethod
    def register_artifact(self, artifact_input: ArtifactsInput) -> str:
        """
        Saves the artifact information to the artifact store.

        Args:
            artifact_input: An instance of ArtifactsInput containing artifact details.
        Returns:
            a unique artifact_id for the saved artifact.
        """
        ...

    @abstractmethod
    def get_artifact(self, artifact_id: str) -> ArtifactsOutput:
        """
        Retrieves the artifact information from the artifact store.

        Args:
            artifact_id: The unique identifier of the artifact to retrieve.
        Returns:
            An instance of ArtifactsOutput containing the retrieved artifact details.
        """
        ...
