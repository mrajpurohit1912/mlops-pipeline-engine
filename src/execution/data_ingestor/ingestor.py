import pandas as pd
from pathlib import Path

from execution.data_ingestor.base import DataIngestorBase
from core.tasks import CSVIngestorTask
from core.task_base import TaskBase

class CsvIngestor(DataIngestorBase):
    
    def load(self,data_path:Path)->TaskBase:
            return  CSVIngestorTask(data_path)
            
    
