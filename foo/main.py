#!/usr/bin/env python3

"""
here is a simple main() module -- to demonstrate setuptools entrypoints
"""

import sys
import os
import logging

from .foomod import make_foo


def main():
    print("name: " + __name__)
    print("package: " + __package__)

    # This sets the root logger.
    # logger = logging.basicConfig(level=logging.DEBUG)

    logger = logging.getLogger(__package__)
    logger.setLevel(level=logging.DEBUG)
    # Processing basically stops at the first logger with a handler.
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    make_foo()
