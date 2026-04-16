import json
from pathlib import Path

from core.artifacts_core.models import ArtifactsOutput


class LocalStore:
    """
    A local storage for saving artifact metadata in a JSON file.
    """

    def __init__(self, store_path: str):
        self.store_path = Path(store_path)
        self.store_path.mkdir(parents=True, exist_ok=True)
        self._db_path = self.store_path / "artifacts.json"
        if not self._db_path.exists():
            with open(self._db_path, "w") as f:
                json.dump({}, f)

    def _read_db(self) -> dict:
        try:
            with open(self._db_path) as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def _write_db(self, db: dict) -> None:
        with open(self._db_path, "w") as f:
            json.dump(db, f, indent=4, default=str)

    def save_artifact(self, artifact: ArtifactsOutput) -> None:
        """
        Saves the artifact metadata to the local JSON file.

        Args:
            artifact: An instance of ArtifactsOutput containing artifact details.
        """
        db = self._read_db()
        db[artifact.artifact_id] = artifact.dict()
        self._write_db(db)

    def get_artifact(self, artifact_id: str) -> ArtifactsOutput | None:
        """
        Retrieves the artifact metadata from the local JSON file.

        Args:
            artifact_id: The unique identifier of the artifact to retrieve.
        Returns:
            An instance of ArtifactsOutput containing the retrieved artifact details,
            or None if the artifact is not found.
        """
        db = self._read_db()
        artifact_data = db.get(artifact_id)
        if artifact_data:
            return ArtifactsOutput(**artifact_data)
        return None
