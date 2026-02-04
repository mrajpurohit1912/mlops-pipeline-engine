create schema for yaml/json


1. Create Configuration Engine Module(done)

    How to implement?
    -> Create a class for yaml and json parser
    -> Create a schema validator class
    -> Create a env resolver class
    -> Create a DAG Generator class(plan generator)

    NOTE: 
    1.but first create the schema for yaml/json(Done)
    2.also decide what is plan(done, list of task)
    (if not the best create the basic first)

    it will return the plan on the basis of input give by user via YAML/JSON. 

2. Create Pipeline orchestrator Engine Module(done)
    It will receive plan from configuration engine

    How to implement?
    -> Create a Task Scheduler Class
    -> Create a State Manager Class
    -> Create a Retry and Recovery Class

    this module will schedule the task and monitor it

    NOTE: need to decide write this logic manually or use Industry Available tools

3. Create Data Validator Module inside Execution engine module

    there are many kind of validation so create a base.py,validators.py and a factory class and a main.py class which will be used in dag_generator


today todo list
1. how to inject df in validator(done)
2. add scheme validator and dtype validator(done datatype validator and missing value validator)
3. decide what and how will be the output of data validation layer
4. add test and logging as per industry standards(logging is done tests are pending)
5. make orchestrator as per industry standard. by using industry standard tools or by custom logic.
6. add artifacts module to save the artifacts at each stage.
7. decide what will be the output of each module or stage like an html,pdf,pipeline summary or anything else
 
 
 
today todo list
1. every task should return metadata so decide how it would look.
2. in orchestrator add a feature to check the status of as task(state manager) , schedule a task , retry policy   , and 
3. add a metadata store to store the status of pipeline so even if it fails state can be preserved

Current Problem: 
    plan from dag_generator needs to be at needs to be at bigger level like data_ingestion,data_validation,data_cleaning,eda,model_training,model_evaluator,etc.

    currently it is as very small level like csv_ingestor_task,missing_value_task
Current Solution:
    create classes for data_ingestion,data_validation,data_cleaning,eda,model_training,model_evaluator,etc. which will interact with the dag_generator and dag_generator will make a plan which will be passed on to orchestrator.


Level,Name,Responsibility,Example
Level 1,Pipeline,The end-to-end workflow.,TabularClassificationPipeline
Level 2,Stage,A logical group of related operations.,DataValidationStage
Level 3,Task,The atomic execution unit.,DataTypeValidatorTask

# todays todo list
1. add stages on top of task which will interact with orchestrator and not tasks itself

2. refactor orchestrator to check the status of as task(state manager) , schedule a task , retry policy

3. add artifacts module to save the artifacts at each stage.

4. add context in pipeline(avoid passing dfs between stages as context instead create model)

# today todo 
1. make the input yaml/json into a uniform format.