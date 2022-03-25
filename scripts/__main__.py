from arg_parse import parse_args
import client
import logger
import server


# globals
logger = logger.Logger("Core")


def main():
    """
    Entry point
    """
    args = parse_args()

    match args.mode:
        case "server":
            logger.log("Is server")

            server = server.Server(args.ip, args.port)

        case "client":
            logger.log("Is client")

            client = client.Client()


if __name__ == "__main__":
    main()
