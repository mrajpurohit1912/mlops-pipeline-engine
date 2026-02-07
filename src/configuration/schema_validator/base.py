from abc import ABC, abstractmethod
from collections.abc import Mapping


class SchemaValidatorBase(ABC):
    @abstractmethod
    def validate(self, raw_config: Mapping[str, object]) -> None: ...
