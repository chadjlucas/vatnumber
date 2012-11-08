#!/usr/bin/env python
#This file is part of vatnumber.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

import os
from setuptools import setup, find_packages
import vatnumber


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='vatnumber',
    version=vatnumber.__version__,
    author='B2CK',
    author_email='info@b2ck.com',
    url="http://code.google.com/p/vatnumber/",
    description="Python module to validate VAT numbers",
    long_description=read('README'),
    download_url="http://code.google.com/p/vatnumber/downloads/",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    license='GPL-3',
    extras_require={
        'suds': ['suds'],
        },
    test_suite="vatnumber.tests",
    )
