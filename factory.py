import config
import logging
from logo.logging import logger

from logo.centralized_log_service.custom_logger_handler import CustomLoggerHandler
from logo.tcp_logger.tcp_log_handler import TcpLogHandler
from logo.tcp_logger.threaded_tcp_log_server import ThreadedTcpLogServer


def make_app(app_config: config.BaseConfig = None):
    app_config = app_config or config.LOGO_CONFIG
    init_logger(logger, app_config)
    server_address: tuple[str, int] = (app_config.HOST_NAME, app_config.PORT)
    return ThreadedTcpLogServer(server_address, TcpLogHandler)


def init_logger(logger: logging.Logger, app_config: config.BaseConfig = None):
    app_config = app_config or config.LOGO_CONFIG
    formatter = logging.Formatter(app_config.LOG_FORMAT)
    custom_logger_handler = CustomLoggerHandler(app_config.CENTRALIZED_LOG_SERVICE_ADDRESS,
                                                app_config.CENTRALIZED_LOG_SERVICE_PORT)
    custom_logger_handler.setFormatter(formatter)
    logger.addHandler(custom_logger_handler)
    logger.setLevel(app_config.LOG_LEVEL)
