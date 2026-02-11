import logging

from core.stages.base import StageBase

logger = logging.getLogger(__name__)


class DataIngestionStage(StageBase):
    """
    A pipeline stage for ingesting data.
    """

    name = "data_ingestion_stage"
    depends_on = None
    tasks = []


class DataValidationStage(StageBase):
    """
    A pipeline stage for validating data.
    """

    name = "data_validation_stage"
    depends_on = ["data_ingestion_stage"]
    tasks = []
