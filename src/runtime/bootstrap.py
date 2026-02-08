import os

from app_config import Config
from utils.logger import setup_logging


class RuntimeBootstrapper:
    def __init__(self, config: Config):
        self.config = config

    def bootstrap(self) -> None:
        setup_logging()

        for path in self.config.runtime_paths():
            os.makedirs(path, exist_ok=True)
