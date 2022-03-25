import logger


# globals
logger = logger.Logger("Core")


def main():
    logger.log("Hello,", "World!")
    logger.warning("Hello,", "World!")
    logger.error("Hello,", "World!")


if __name__ == "__main__":
    main()
