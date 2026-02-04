# from pathlib import Path

# import polars as pl

# from core.base import TaskBase
# from core.models.models import TaskExecutionResult, TaskMetaData


# class CSVIngestorTask(TaskBase):
#     def __init__(self, path: Path):
#         self.path = path
#         self.name = "csv_ingestion"
#         self.depends_on = None

#     def __prepare_metadata(self) -> TaskMetaData:
#         return TaskMetaData(
#             pipeline_run_id="demo_id",
#             task_name=self.name,
#             status="COMPLETED",
#             error_message=None,
#         )

#     def run(self, context: dict | None = None) -> TaskExecutionResult:
#         try:
#             result = self.execute(context)
#             return TaskExecutionResult(
#                 metadata=self.__prepare_metadata(), result=result
#             )
#         except Exception as e:
#             return TaskExecutionResult(error=str(e))

#     def execute(self, context: dict | None = None) -> pl.DataFrame:
#         df = pl.read_csv(self.path)
#         return df


# class MissingValueValidatorTask(TaskBase):
#     def __init__(self, missing_percentage_value: float):
#         self.missing_percentage_value = missing_percentage_value
#         self.name = "missing_value_validator"
#         self.depends_on = ["csv_ingestion"]

#     def _prepare_metadata(self) -> TaskMetaData:
#         return TaskMetaData(
#             pipeline_run_id="demo_id",
#             task_name=self.name,
#             status="COMPLETED",
#             error_message=None,
#         )

#     def run(self, context: dict | None = None) -> TaskExecutionResult:
#         try:
#             result = self.execute(context)
#             return TaskExecutionResult(metadata=self._prepare_metadata(), result=result)
#         except Exception as e:
#             return TaskExecutionResult(status=False, error=str(e))

#     def execute(self, context: dict | None = None) -> pl.DataFrame:
#         df = context["csv_ingestion"]
#         missing_value_info = (df.null_count() / len(df)) * 100

#         for col in missing_value_info.columns:
#             if missing_value_info[col][0] > self.missing_percentage_value:
#                 # print(f"Column {col} has {missing_value_info[col][0]}% missing values, dropping it.")
#                 df = df.drop(col)
#         return df


# class DataTypeValidatorTask(TaskBase):
#     def __init__(self, column_config: dict):
#         self.column_config = column_config
#         self.name = "data_type_validator"
#         self.depends_on = ["missing_value_validator"]

#     def run(self, context: dict | None = None) -> TaskExecutionResult:
#         df = context["missing_value_validator"]

#         polars_type_map = {
#             "int": pl.Int64,
#             "str": pl.Utf8,
#             "float": pl.Float64,
#         }

#         for col_info in self.column_config.values():
#             col_name = col_info.name
#             expected_dtype_str = col_info.dtype

#             if col_name in df.columns:
#                 expected_dtype = polars_type_map.get(expected_dtype_str)
#                 if expected_dtype and df[col_name].dtype != expected_dtype:
#                     print(
#                         f"Warning: Column '{col_name}' has type {df[col_name].dtype} but expected {expected_dtype}."
#                     )
#                     # try:
#                     #     df = df.with_columns(pl.col(col_name).cast(expected_dtype, strict=False))
#                     # except Exception as e:
#                     #     print(f"Error casting column '{col_name}': {e}")
#         return df



# This file is intentionally left blank as part of a refactoring.
# The abstractions that were here (`DataIngestorTask`, `ValidatorTask`) have been removed.
# Concrete task implementations in the `execution` module should now inherit
# directly from `core.tasks.base.TaskBase`.
