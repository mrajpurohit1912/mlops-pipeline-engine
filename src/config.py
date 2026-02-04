from dataclasses import dataclass
from pathlib import Path

from pyprojroot import find_root, has_file


@dataclass
class Config:
    ROOT_PATH: Path = find_root(has_file("pyproject.toml"))
    CLASSIFICATION_PIPELINE_CONFIG_PATH: Path = (
        ROOT_PATH
        / "src"
        / "configs"
        / "pipelines"
        / "tabular_classification_pipeline.yaml"
    )
