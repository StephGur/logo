from socketserver import ThreadingTCPServer


class ThreadedTcpLogServer(ThreadingTCPServer):
    def __init__(self, server_address: tuple[str, int], log_handler):
        super().__init__(server_address, log_handler)
