from abc import ABC, abstractmethod


class BaseCentralizedLogServiceInitiator(ABC):
    def __init__(self, service_address: str, service_port: int):
        self.address = service_address
        self.port = service_port

    @abstractmethod
    def init_service(self):
        pass


class LogStashLogService(BaseCentralizedLogServiceInitiator):
    def init_service(self):
        # using the parent parameters to connect to a real service
        # right now it's a mock that contains a print and should return the instance or somthing of the service
        print(f'service address: {self.address}, service port: {self.port}')
        return self

    def send_request(self, message: str):
        # Here should be the implementation of the communication with logstash using the requests library
        # Meaning it throws RequestException
        print(f'Sending log message: {message}')
