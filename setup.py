#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="tracker", packages=find_packages(where="src"), package_dir={"": "src"})
