from pathlib import Path
from abc import ABC,abstractmethod

# from configuration.models.config_model import MLConfig

class ParserBase(ABC):

    @abstractmethod
    def parse(self,config_path:Path)-> dict:
        pass