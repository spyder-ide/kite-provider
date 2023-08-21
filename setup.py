# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2022, spyder-vim
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
spyder-vim setup.
"""
import io
from setuptools import find_packages
from setuptools import setup

# =============================================================================
# Use Readme for long description
# =============================================================================
with io.open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="kite-provider",
    version="0.1.0",
    author="",
    author_email="spyder.python@gmail.com",
    description="A plugin to enable kite provider to the spyder editor",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT license",
    url="https://github.com/spyder-ide/spyder-vim",
    python_requires=">= 3.7",
    install_requires=[
        "qtpy",
        "qtawesome",
        "spyder>=5.3.3",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": ["kite = spyder.plugins.completion.providers.kite.provider:"
                           "KiteProvider"],
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)",
    ],
)