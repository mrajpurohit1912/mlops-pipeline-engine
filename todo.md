create schema for yaml/json


1. Create Configuration Engine Module

    How to implement?
    -> Create a class for yaml and json parser
    -> Create a schema validator class
    -> Create a env resolver class
    -> Create a DAG Generator class(plan generator)

    NOTE: 
    1.but first create the schema for yaml/json
    2.also decide what is plan(e.g a dict, or something else)
    (if not the best create the basic first)

    it will return the plan on the basis of input give by user via YAML/JSON. 

2. Create Pipeline orchestrator Engine Module
    It will receive plan from configuration engine

    How to implement?
    -> Create a Task Scheduler Class
    -> Create a State Manager Class
    -> Create a Retry and Recovery Class

    this module will schedule the task and monitor it

    NOTE: need to decide write this logic manually or use Industry Available tools
