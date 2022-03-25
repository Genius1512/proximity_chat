from socket import *

import logger


class Server(socket):
    """
    Server class
    """
    def __init__(self, ip: str, port: int):
        """
        Construct a server

        :param ip: The IP the server will be setup on
        :type ip: str

        :param port: The port the server will be setup on
        :type port: int

        :return: None
        :rtype: None
        """
        self.logger = logger.Logger("Server")
        
        super().__init__()
        self.bind((ip, port))
        self.logger.log("Server setup")


        self.ip = ip
        self.port = port

