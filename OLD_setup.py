"""
DEPRECATED
Pip wasn't happy installing using this so I'm disabling this so that it forces
to use the pyproject.toml
"""

#!/usr/bin/env python3
# Inspired from https://github.com/kennethreitz/setup.py

from pathlib import Path
from setuptools import setup, find_packages

NAME = "RobAuraLoss"
DESCRIPTION = "Audio-focused loss functions in PyTorch"
URL = "https://github.com/MxRobsta/RobAuraLoss"
EMAIL = "rwhsutherland1@sheffield.ac.uk"
AUTHOR = "Robbie Sutherland"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.4.0"

HERE = Path(__file__).parent

try:
    with open(HERE / "README.md", encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["RobAuraLoss"],
    install_requires=["torch", "numpy", "setuptools"],
    extras_require={"test": ["resampy"], "all": ["matplotlib", "librosa", "scipy"]},
    include_package_data=True,
    license="Apache License 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Scientific/Engineering",
    ],
)
