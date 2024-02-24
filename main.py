import logging

import config
from logo.logger import CustomLoggerHandler
from logo.tcp_log_handler import TcpLogHandler
from logo.tcp_log_server import ThreadedTcpLogServer


def init_logger():
    formatter = logging.Formatter(config.LOGO_CONFIG.LOG_FORMAT)
    custom_logger_handler = CustomLoggerHandler(config.LOGO_CONFIG.CENTRALIZED_LOG_SERVICE_ADDRESS,
                                                config.LOGO_CONFIG.CENTRALIZED_LOG_SERVICE_PORT)
    custom_logger_handler.setFormatter(formatter)
    logger = logging.getLogger('lol')
    logger.addHandler(custom_logger_handler)
    logger.setLevel(config.LOGO_CONFIG.LOG_LEVEL)


if __name__ == "__main__":
    init_logger()
    server_address: tuple[str, int] = (config.LOGO_CONFIG.HOST_NAME, config.LOGO_CONFIG.PORT)
    with ThreadedTcpLogServer(server_address, TcpLogHandler) as server:
        server.serve_forever()


