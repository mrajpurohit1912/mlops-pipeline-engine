from core.task_base import TaskBase

class PipelineOrchestrator:
    def run(self,tasks:list[TaskBase]):
        for task in tasks:
            result = task.run()
            print(result)