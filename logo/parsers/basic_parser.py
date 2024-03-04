from datetime import datetime

from logo.helpers import LogLevel, is_valid_ip, TIME_FORMAT, is_valid_port


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

        parsed_result = LogMessageResult(str(log_message['message']))
        parsed_result.log_level = log_message.get('logLevel', LogLevel.INFO.value)

        self._validate_ip(log_message, parsed_result)
        self._validate_port(log_message, parsed_result)

        return parsed_result

    def _validate_port(self, log_message: dict, parsed_result: LogMessageResult):
        if 'logServicePort' in log_message:
            log_service_port = log_message['logServicePort']
            if not isinstance(log_service_port, int) or not is_valid_port(log_service_port):
                raise LogMessageParserError("Please provide a valid port")
            else:
                parsed_result.log_service_port = log_service_port

    def _validate_ip(self, log_message: dict, parsed_result: LogMessageResult):
        if 'logServiceAddress' in log_message:
            log_service_address = log_message['logServiceAddress']
            if not isinstance(log_service_address, str) or not is_valid_ip(log_service_address):
                raise LogMessageParserError("Please provide a valid ip address")
            else:
                parsed_result.log_service_address = log_message['logServiceAddress']
