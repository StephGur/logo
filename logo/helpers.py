import ipaddress
from enum import Enum

from logo.logging import logger


def is_valid_ip(ip: str) -> bool:
    try:
        # Attempt to create an IPv4 or IPv6 object from the input
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        # ValueError is raised if the input is not a valid IP address
        return False


def is_valid_port(port: int):
    if 1 <= port <= 65535:
        return True

    return False


TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"


class LogLevel(Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    ERROR = 'ERROR'
    EXCEPTION = 'EXCEPTION'


log_to_level = {
    LogLevel.DEBUG.value: logger.debug,
    LogLevel.INFO.value: logger.info,
    LogLevel.ERROR.value: logger.error,
    LogLevel.EXCEPTION.value: logger.exception
}
