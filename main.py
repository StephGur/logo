import csv
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
from socketserver import BaseRequestHandler, ThreadingTCPServer, TCPServer


class LogWriter(ABC):
    def __init__(self, message: str):
        self.message = message
        super().__init__()

    @abstractmethod
    def handle(self):
        pass


class FileWriter(LogWriter):
    def __init__(self, message: str, file_name: str = "logs.txt"):
        super().__init__(message)
        self.file_name = file_name

    def handle(self):
        with open(self.file_name, 'w') as f:
            f.write(self.message)


class TcpLogHandler(BaseRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(1024).strip()
        timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_ip: str = self.client_address[0]
        log_message: str = f"[{timestamp}] : {client_ip} : {data}"
        print(f"Received log: {log_message}")
        self.write_log()

    def write_log(self):
        pass


class TcpLogServer(TCPServer):
    def __init__(self, server_address: tuple[str, int], request_handler):
        super().__init__(server_address, request_handler)


if __name__ == "__main__":
    listen_port = 1313
    log_service_ip = 'steph'
    log_service_port = '1234'
    handler = TcpLogHandler

    server_address: tuple[str, int] = ('localhost', listen_port)
    with TcpLogServer(server_address, handler) as server:
        server.serve_forever()


