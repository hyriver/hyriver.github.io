#!/usr/bin/env python
"""The setup script."""
from setuptools import setup
from pathlib import Path


with open(Path(__file__).with_name("README.rst")) as f:
    long_description = f.read()

setup(
    name="HyRiver",
    version="0.0.0",
    long_description=long_description,
    long_description_content_type="text/x-rst",
)
