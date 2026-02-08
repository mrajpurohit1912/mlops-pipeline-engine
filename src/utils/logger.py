import logging
import logging.config
import sys

from pythonjsonlogger import jsonlogger


def setup_logging(env: str = "dev", service: str = "dynamic-mlops"):
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": jsonlogger.JsonFormatter,
                "format": (
                    "%(asctime)s "
                    "%(levelname)s "
                    "%(name)s "
                    "%(funcName)s "
                    "%(lineno)d "
                    "%(message)s "
                    "%(process)d "
                    "%(threadName)s "
                    "%(env)s "
                    "%(service)s "
                    "%(run_id)s"
                ),
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "level": "INFO",
                "stream": sys.stdout,
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "json",
                "level": "INFO",
                "filename": "app.log",
                "maxBytes": 10_485_760,
                "backupCount": 5,
                "encoding": "utf8",
            },
        },
        "root": {
            "handlers": ["console", "file"],
            "level": logging.DEBUG,
        },
    }

    logging.config.dictConfig(logging_config)

    logging.LoggerAdapter(
        logging.getLogger(),
        {
            "env": env,
            "service": service,
            "run_id": "bootstrap",
        },
    )
