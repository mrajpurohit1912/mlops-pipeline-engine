from dataclasses import dataclass
from pathlib import Path

from pyprojroot import find_root, has_file


@dataclass
class Config:
    env = "dev"
    ROOT_PATH: Path = find_root(has_file("pyproject.toml"))

    LOCAL_DATA_ROOT_PATH: Path = ROOT_PATH / "data"
    LOCAL_DATA_RAW_PATH: Path = LOCAL_DATA_ROOT_PATH / "raw"
    LOCAL_DATA_PROCESSED_PATH: Path = LOCAL_DATA_ROOT_PATH / "processed"
    LOCAL_ARTIFACTS_ROOT_PATH: Path = ROOT_PATH / "artifacts"

    DATASTORAGE_ARTIFACT_BASE_PATH: Path = ROOT_PATH / "datastorage_artifacts"
    


    def runtime_paths(self) -> list[Path]:
        return [
            self.LOCAL_DATA_ROOT_PATH,
            self.LOCAL_DATA_RAW_PATH,
            self.LOCAL_DATA_PROCESSED_PATH,
            self.LOCAL_ARTIFACTS_ROOT_PATH,
        ]
