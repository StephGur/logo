from datetime import datetime
from socketserver import BaseRequestHandler

from logo.logging import logger

TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"


class TcpLogHandler(BaseRequestHandler):
    def handle(self) -> None:
        formatted_message: str = self._format_message()
        self._write_log(formatted_message)
        self.request.send('OK'.encode('utf-8'))

    def _format_message(self) -> str:
        message: str = self.request.recv(1024).strip()
        timestamp: str = datetime.now().strftime(TIME_FORMAT)
        client_ip: str = self.client_address[0]
        formatted_log_message: str = f"[{timestamp}] | {client_ip} | {message}"
        return formatted_log_message

    def _write_log(self, message: str):
        logger.info(message)
