#!/usr/bin/env python

from setuptools import setup

setup(name='foo',
      version='1.0',
      # list folders, not files
      packages=['foo'],
      scripts=['foo/bin/foo_script.py'],
      install_requires=[
        'requests>=2.20.0',
      ],
      )
