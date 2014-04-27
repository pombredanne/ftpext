#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

setup(
    name='ftpext',
    version='0.1.0',
    description='extensions to the \'ftplib\' module',
    long_description=readme,
    author='Kalle Lindqvist',
    author_email='',
    url='https://github.com/kalind/ftpext',
    packages=[
        'ftpext',
    ],
    package_dir={'ftpext': 'ftpext'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='ftpext, FTP, client, library',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
)
