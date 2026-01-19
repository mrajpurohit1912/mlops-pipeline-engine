from pathlib import Path
from pyprojroot import has_file,find_root
from dataclasses import dataclass

@dataclass
class Config():
    ROOT_PATH:Path = find_root(has_file("pyproject.toml"))
    CLASSIFICATION_PIPELINE_CONFIG_PATH:Path = ROOT_PATH / "src" / "configs" / "pipelines" / "tabular_classification_pipeline.yaml"
   