from execution.data_ingestor.base import DataIngestorBase
from execution.data_ingestor.ingestor import CsvIngestor

class DataIngestorFactory:

    @staticmethod
    def get_ingestor(source_type:str)->DataIngestorBase:
            if source_type == "csv":
                return CsvIngestor()