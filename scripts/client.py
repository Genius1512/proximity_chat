from socket import *

import logger


class Client(socket):
    def __init__(self):
        super().__init__()

        self.logger = logger.Logger("Client")

    def connect(self, ip: str, port: int):
        self.connect((ip, port))
