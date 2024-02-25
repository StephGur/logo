import os


class BaseConfig:
    TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_LEVEL = 'INFO'


class LocalConfig(BaseConfig):
    HOST_NAME = 'LOCALHOST'
    PORT = 1313
    CENTRALIZED_LOG_SERVICE_PORT = os.getenv('CENTRALIZED_LOG_SERVICE_PORT') or 8080
    CENTRALIZED_LOG_SERVICE_ADDRESS = os.getenv('CENTRALIZED_LOG_SERVICE_ADDRESS') or '1.1.1.1'


def get_configuration_by_name(environment: str = 'DEFAULT') -> BaseConfig:
    return {
        'LOCAL': LocalConfig,
        'DEFAULT': LocalConfig
    }[environment]


def get_configuration() -> type(BaseConfig):
    environment: str = os.getenv('SOCKET', 'DEFAULT')
    return get_configuration_by_name(environment)


LOGO_CONFIG = get_configuration()
