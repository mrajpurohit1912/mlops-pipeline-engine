import pandas as pd
from pathlib import Path
from core.task_base import TaskBase

class CSVIngestorTask(TaskBase):
    def __init__(self,path:Path):
        self.path = path
        self.name = "csv_ingestion"
        self.depends_on = None

    def run(self):
        return pd.read_csv(self.path)