from pathlib import Path
from utils.dataset_manager.dataset_manager import (
    DatasetManagerTabular,
    DatasetManagerImage,
)


class DatasetManagerFactory:
    def get_dataset_manager(dataset_type: str,base_path:Path):
        if dataset_type == "tabular":
            return DatasetManagerTabular(base_path)
        elif dataset_type == "image":
            return DatasetManagerImage(base_path)
        else:
            raise ValueError(f"Unsupported dataset type: {dataset_type}")

    