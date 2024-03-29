#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine
# python setup.py sdist upload -r pypi

import io
import os

from distutils.core import setup

# Package meta-data.
NAME = 'invincible9889'
DESCRIPTION = 'An incincible package'
URL = 'https://github.com/Louis0124/invincible'
EMAIL = 'ZK@zk.com'
AUTHOR = 'ZK'
REQUIRES_PYTHON = '>=3.4.0'
VERSION = "1.1.1"

# What packages are required for this module to be executed?
REQUIRED = [
    "tornado",
    "beautifulsoup4",
    "requests",
    "redis"
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README.md and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    # long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['invincible'],
    install_requires=REQUIRED,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # data_files=['README.rst']
)