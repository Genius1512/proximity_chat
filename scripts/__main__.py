from arg_parse import parse_args
from client import Client
import logger
from server import Server


# globals
logger = logger.Logger("Core")


def main():
    """
    Entry point
    """
    args = parse_args()

    if args.mode == "server":
        logger.log("Is server")

        server = Server(args.ip, args.port)

    elif args.mode == "client":
        logger.log("Is client")

        client = Client(args.ip, args.port)


if __name__ == "__main__":
    main()
