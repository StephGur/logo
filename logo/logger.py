from logging import StreamHandler, LogRecord

from requests import RequestException

from logo.base_centralized_log_service import LogStashLogService


class CustomLoggerHandler(StreamHandler):
    def __init__(self, address: str, port: int):
        super().__init__()
        self.centralized_log_service = LogStashLogService(address, port).init_service()

    def emit(self, record: LogRecord) -> None:
        message = self.format(record)
        try:
            self.centralized_log_service.send_request(message)
        except RequestException as e:
            self.stream.write(f'Failed sending message to logstash {str(e)}')
