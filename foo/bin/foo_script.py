#!/usr/bin/env python3

"""
A really simple script just to demonstrate packaging
"""

import sys, os
from foo import main


if __name__ == "__main__":
    print("foo_script: " + __name__)
    main.main()
