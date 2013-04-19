#!/usr/bin/env python

from setuptools import setup, find_packages

name = "syllabizer"

setup(
    name = name,
    version = "0.2.1",
    url = "http://silpa.org.in/Syllabize",
    license = "LGPL-3.0",
    description =  "Syllabify each word in the given text",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description =   "Syllabify each word in the given text",
    packages = find_packages('.'),
    package_data = {'.':[]},
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools'],
    zip_safe = False,
    )
