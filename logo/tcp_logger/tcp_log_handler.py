import json
from socketserver import BaseRequestHandler

from config import LOGO_CONFIG
from logo.helpers import log_to_level
from logo.parsers.basic_parser import BasicLogMessageParser, LogMessageResult, LogMessageParserError

TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"


class TcpLogHandler(BaseRequestHandler):
    _parsers = {
       'BASIC': BasicLogMessageParser()
    }

    def handle(self) -> None:
        try:
            parsed_log_message: LogMessageResult = self._parse_log_message()
            self._write_log(parsed_log_message)
            self.request.send('OK'.encode('utf-8'))
        except LogMessageParserError as e:
            self.request.send(str(e).encode('utf-8'))

    def _get_parser(self, parser_type: str = None) -> BasicLogMessageParser:
        return self._parsers[LOGO_CONFIG.LOG_PARSER or parser_type]

    def _parse_log_message(self) -> LogMessageResult:
        parser = self._get_parser()

        try:
            message: dict = json.loads(self.request.recv(1024).strip())
            parsed_log_message: LogMessageResult = parser.parse(message)
            return parsed_log_message
        except ValueError as e:
            raise LogMessageParserError("Please Provide a valid json!") from e

    def _format_message_new(self, parsed_log_message: LogMessageResult):
        client_ip: str = self.client_address[0]
        return f"{client_ip} | {parsed_log_message.build_result_string()}"

    def _write_log(self, parsed_message: LogMessageResult):
        log_to_level[parsed_message.log_level](self._format_message_new(parsed_message))
