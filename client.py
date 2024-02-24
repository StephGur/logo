import socket


def send_log_message(message: str, server_address: str, server_port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_address, server_port))
        client_socket.send(message.encode('utf-8'))


if __name__ == "__main__":
    server_address = 'localhost'
    server_port = 1313

    while True:
        try:
            message = dict(input("Your Log: "))
            send_log_message(message, server_address, server_port)
        except KeyboardInterrupt:
            print("Finished sending your logs")
