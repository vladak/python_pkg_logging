import os
import logging

from requests import get


def make_foo():
    print(__name__)
    print("foo!")

    logger = logging.getLogger(__name__)
    logger.debug("foo debug")

    r = get('http://grok.cz.oracle.com')
    print(r)
