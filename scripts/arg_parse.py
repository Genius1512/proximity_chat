from argparse import ArgumentParser, ArgumentTypeError
import re


def mode(arg: str) -> str:
    return arg.lower()


def ip(arg: str) -> str:
    pattern = re.compile(r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}")
    if re.match(pattern, arg):
        return arg
    else:
        raise ArgumentTypeError(f"Invalid ip '{arg}'")


def port(arg: str) -> int:
    try:
        arg = int(arg)
    except ValueError:
        raise ArgumentTypeError(f"Invalid port '{arg}'")

    return arg


def parse_args():
    parser = ArgumentParser(description="Argument Parser")

    parser.add_argument(
        "mode",
        type=mode,
        choices=["server", "client"],
        help="Server or client"
    )

    parser.add_argument(
        "--ip",
        type=ip,
        help="IP"
    )

    parser.add_argument(
        "-p", "--port",
        type=port,
        help="Port"
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = vars(parse_args())
    for key in args:
        print(f"{key}: {args[key]}")
