from factory import make_app

threaded_tcp_log_server = make_app()


if __name__ == "__main__":
    with threaded_tcp_log_server as server:
        server.serve_forever()
