from pathlib import Path
from abc import ABC,abstractmethod

class DataIngestorBase(ABC):
    
    @abstractmethod
    def load(self,data_path:Path):
        pass