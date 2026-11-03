from pathlib import Path
from abc import ABC, abstractmethod

from core.dataset_core.dto import DatasetSaveRequest


class DatasetManagerBase(ABC):
    """
    Base class for dataset management operations.
    """

    def __init__(self,base_path:Path):
        self.base_path = base_path

    @abstractmethod
    def save_dataset(
        self,
        dataset:object, 
        request:DatasetSaveRequest,
    )->Path:
        """
        Saves a dataset to the specified path.
        """
        pass

    @abstractmethod
    def load_dataset(self,
                     path: str,):
        """
        Loads a dataset from the specified path.
        """
        pass