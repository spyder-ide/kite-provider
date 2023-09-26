# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2022, kite-provider
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
kite-provider setup.
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
    version="0.1.0dev0",
    author="Spyder Project Contributors",
    author_email="spyder.python@gmail.com",
    description="Kite completions provider for Spyder",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT license",
    url="https://github.com/spyder-ide/kite-provider",
    python_requires=">= 3.7",
    install_requires=[
        "qtpy",
        "qtawesome",
        "psutil",
        "spyder>=6.0",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.completions": ["kite = kite_provider.provider:"
                           "KiteProvider"],
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)",
    ],
)