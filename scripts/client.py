from socket import *
from atexit import register

import logger


class Client(socket):
    def __init__(self, ip: str, port: int):
        super().__init__()
        register(self.close)

        self.logger = logger.Logger("Client")

        self.ip = ip
        self.port = port
        self.is_connected = False

    def connect(self):
        self.connect((self.ip, self.port))
        self.is_connected = True

    def close(self):
        super().close()

    def __repr__(self):
        if self.is_connected:
            return f"Client connected to {self.ip}:{self.port}"
        else:
            return f"Client connecting to {self.ip}:{self.port}"
