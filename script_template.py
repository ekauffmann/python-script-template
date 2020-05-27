#!/usr/bin/python

import argparse
from datetime import datetime, timezone
import json
import os
from random import SystemRandom
import sys
import time
from typing import Text


def main(
    string_arg: Text, bool_arg: bool, int_arg: int = 100, verbose: bool = False,
) -> None:
    try:
        pass
    except KeyboardInterrupt:
        if verbose:
            print("Stopping...")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="script_template",
        description="Template for python scripts with argument parsing.",
    )
    parser.add_argument("-s", "--string_arg", type=str, help="help text")
    parser.add_argument(
        "-b", "--bool_arg", action="store_true", help="flag stored as true if present"
    )
    parser.add_argument("-i", type=int, help="integer arg")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")

    args = parser.parse_args()

    string_arg = args.string_arg or "123456789_fake_dev"
    bool_arg = args.bool_arg
    int_arg = args.i or 100
    verbose = args.verbose
    main(string_arg, bool_arg, int_arg, verbose)
