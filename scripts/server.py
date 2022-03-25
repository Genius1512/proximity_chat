from socket import *


class Server(socket):
    def __init__(self, ip: str, port: int):
        super().__init__()
        self.bind((ip, port))

        self.ip = ip
        self.port = port

