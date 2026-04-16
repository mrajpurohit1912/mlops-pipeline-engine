from pathlib import Path
import polars as pl


from utils.dataset_manager.base import DatasetManagerBase
from utils.dataset_manager.dto import DatasetSaveRequest




class DatasetManagerTabular(DatasetManagerBase):
    """
    Implementation of DatasetManager for handling dataset I/O operations.
    """

    def save_dataset(self, dataset:pl.DataFrame,request:DatasetSaveRequest ):
        """
        Saves a dataset (e.g., Polars DataFrame) to the specified path in parquet format.
        """
        dataset_path = (
            self.base_path 
            / request.dataset_layer 
            / request.execution_date.isoformat() 
            / request.dataset_name
            / request.pipeline_run_id
            / request.version
        )
        
        dataset_path.mkdir(parents=True,exist_ok=True)
        file_path = dataset_path / f"{request.dataset_name}.{request.format}"
        

        if dataset.format == "csv":
            dataset.write_csv(file_path)
        else:   
            dataset.write_parquet(file_path)

        return file_path

    def load_dataset(self, path:Path) -> pl.DataFrame:
        """
        Loads a dataset from the specified path.
        """
        return pl.read_parquet(path)

class DatasetManagerImage(DatasetManagerBase):
    """
    Implementation of DatasetManager for handling image dataset I/O operations.
    """

    def save_dataset(self, dataset, path: str, **kwargs):
        """
        Saves an image dataset to the specified path.
        """
        ...

    def load_dataset(self, path: str, **kwargs):
        """
        Loads an image dataset from the specified path.
        """
        ...
        