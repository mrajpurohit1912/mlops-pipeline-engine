from abc import ABC,abstractmethod

class TaskBase(ABC):
    name:str
    depends_on:list[str] | None

    @abstractmethod
    def run(self):
        pass