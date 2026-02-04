from configuration.schema.input_config_schema import MLConfig
from core.tasks.base import TaskBase
from execution.data_validation.validators import (
    DataTypeValidator,
    MissingValueValidator,
)


class DataValidatorFactory:
    """
    Factory for creating data validation tasks.
    """

    @staticmethod
    def create_tasks(task_name:str,validation_config: MLConfig) -> TaskBase:
        """
        Creates a list of data validation tasks based on the validation config.

        Args:
            validation_config: The validation configuration object.

        Returns:
            A list of configured data validation tasks.
        """
        # tasks = []
        # if not validation_config.enabled:
        #     return tasks

        # if validation_config.missing_value_validation:
        #     tasks.append(
        #         MissingValueValidator(
        #             missing_percentage=validation_config.missing_value_validation.missing_percentage
        #         )
        #     )

        # if validation_config.data_type_validation:
        #     # The schema has a 'columns' attribute which is a dict.
        #     # We need to extract the dtype for each column name.
        #     column_dtype_config = {
        #         v.name: v.dtype
        #         for _, v in validation_config.data_type_validation.columns.items()
        #     }
        #     tasks.append(DataTypeValidator(column_config=column_dtype_config))

        # return tasks


        if task_name == "missing_value_validator":
            return MissingValueValidator(
                missing_percentage=validation_config.data_validation.missing_value_validation.missing_percentage
            )
        elif task_name == "data_type_validator":
            return DataTypeValidator(
                column_config=validation_config.data_validation.data_type_validation.columns
            )
        else:
            raise ValueError(f"Unsupported validator type: {task_name}")
        


