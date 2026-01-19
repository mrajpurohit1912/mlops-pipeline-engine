from typing import List

from configuration.models.config_model import MLConfig
from execution.data_ingestor.ingestor import CsvIngestor
from core.task_base import TaskBase
from execution.data_ingestor.factory import DataIngestorFactory

class DAGGenerator:


    def generate(self,config:MLConfig)->List[TaskBase]:
        tasks = []

        ingestor = DataIngestorFactory.get_ingestor(config.data.source.type)
        ingestor_task = ingestor.load(config.data.source.path)
        
        tasks.append(ingestor_task)

        # if config.validation.enabled:
        #     tasks.append()

        return tasks