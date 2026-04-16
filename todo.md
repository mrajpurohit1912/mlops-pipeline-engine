1. Refactor artifacts manager
    - Add support for storing,versioning and maintaing the dataset


Note: each task/stage will return a result.
        result is combination of metadata and the referace 
        and not the output of the task/stage.(so add a dataset menager for storing and retrieving the dataset in utils so that it can be used in different modules of the codebase)

        but if we add a dataset manager, how task will that dataset_manager(we will use dependency injection to inject dataset manager into orchestroation and then futher it will be passed on to stages and then tasks)

        what will be the uri base_path(cloude,local,data warehouse) + dataset_level(raw,processed,final) + todays_date + dataset_type(if tabuler data then parquet,images then what,videos then what and text then what) + pipeline_run_id + versioning 

        then that result will be passed on to artifacts manager

        artifacts manager will be responsible for storing the artifacts,maintaining and versioning of the artifacts.



src/
├── core/
│   ├── dataset/
│   │   ├── base.py          # DatasetManagerBase
│   │   ├── models.py        # DatasetSaveRequest
│   │   └── __init__.py
│   │
│   ├── artifacts/
│   │   ├── base.py
│   │   ├── models.py
│   │
│   ├── execution/
│   │   ├── metadata.py
│   │   └── context.py
│
├── infrastructure/
│   ├── dataset/
│   │   ├── tabular.py       # DatasetManagerTabular
│   │   ├── image.py
│   │   └── __init__.py
│   │
│   ├── artifacts/
│   │   ├── local.py
│   │   ├── mlflow.py
│   │
├── application/
│   ├── factories/
│   │   ├── dataset_factory.py
│   │   ├── artifact_factory.py
│   │
│   ├── orchestrator/
│   │   └── pipeline_orchestrator.py
│
├── tasks/
├── stages/
├── configuration/
└── main.py



src/
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── enums/
│   ├── ports/
│   │   └── artifact_manager.py
│   └── models/
│
├── application/
│   ├── use_cases/
│   ├── services/
│   ├── factories/
│   ├── pipeline/
│   └── config/
│
├── infrastructure/
│   ├── artifact_manager/
│   │   ├── local.py
│   │   ├── s3.py
│   ├── storage/
│   ├── messaging/
│   └── mlflow/
│
├── interfaces/
│   ├── api/
│   ├── cli/
│   └── scheduler/
│
└── main.py
