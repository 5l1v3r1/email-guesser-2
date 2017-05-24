#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from io import open
import sys

setup(
    name='email_guender_guesser',
    version='0.0.1',
    description='',
    install_requires=['gender-guesser'],
    packages=['email_guesser'],
    package_dir={'email_guesser': 'email_guesser'},
)