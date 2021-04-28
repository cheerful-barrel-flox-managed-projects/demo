#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import clinix

setup(
    name="clinix",
    version=clinix.__version__,
    description='Clinix Demo Scripts',
    author='Ben Bell',
    author_email='bellbe@deshaw.com',
    include_package_data=True,
    packages=find_packages(),
    scripts=[
        "clinix-demo",
    ]
)
