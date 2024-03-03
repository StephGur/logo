from datetime import datetime

from logo.helpers import LogLevel, is_valid_ip, TIME_FORMAT


class LogMessageParserError(Exception):
    pass


class LogMessageResult:
    log_level: str = None
    log_service_port: int = None
    log_service_address: str = None

    def __init__(self, message: str, timestamp: str = None):
        self.message = message
        self.timestamp = timestamp or datetime.now().strftime(TIME_FORMAT)

    def build_result_string(self) -> str:
        return f"[{self.timestamp}] | {self.message}"


class BaseLogMessageParser:
    def parse(self, log_message: dict) -> LogMessageResult:
        raise NotImplementedError()


class BasicLogMessageParser(BaseLogMessageParser):
    def parse(self, log_message: dict) -> LogMessageResult:
        if type(log_message) is not dict:
            raise LogMessageParserError("Log message is not a valid object!")

        if 'message' not in log_message:
            raise LogMessageParserError("No message provided! Please provide a message")

        parsed_result = LogMessageResult(log_message['message'])
        parsed_result.log_level = log_message.get('logLevel', LogLevel.INFO.value)
        parsed_result.log_service_port = log_message.get('logServicePort')

        if 'logServiceAddress' in log_message and is_valid_ip(log_message['logServiceAddress']):
            parsed_result.log_service_address = log_message.get('logServiceAddress')

        return parsed_result
