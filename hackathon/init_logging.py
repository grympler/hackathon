import logging

from pythonjsonlogger import jsonlogger


LOG_LEVEL = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


def init_logging(log_level="info", formatter_type=None):
    root_logger = logging.getLogger()

    log_handler = logging.StreamHandler()
    if formatter_type == "json":
        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(filename)-12s %(module)s %(levelname)-8s %(message)s")
    else:
        formatter = logging.Formatter(
            fmt='%(asctime)s :: %(filename)s :: %(name)s :: %(levelname)-6s :: %(message)s'
        )
    log_handler.setFormatter(formatter)
    root_logger.addHandler(log_handler)

    logging.getLogger().setLevel(LOG_LEVEL[log_level])
