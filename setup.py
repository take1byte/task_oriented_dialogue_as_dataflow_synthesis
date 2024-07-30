#!/usr/bin/env python
#  Copyright (c) Microsoft Corporation.
#  Licensed under the MIT license.
from setuptools import find_packages, setup

setup(
    name="sm-dataflow",
    version="0.1",
    author="Semantic Machines (TM)",
    description="Task-Oriented Dialogue as Dataflow Synthesis",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"dataflow": ["py.typed"]},
    zip_safe=False,
    install_requires=[
        "jsons==1.6.3",
        "more-itertools==8.2.0",
        "sexpdata==0.0.3",
        "pandas==2.2.2",
        "spacy==3.7.5",
        "statsmodels==0.14.1",
        "cached-property==1.5.1",
    ],
    extra_requires={
        "OpenNMT-py": ["OpenNMT-py==1.0.0", "pytorch>=1.2.0,<=1.4.0"]
    },
    python_requires=">=3.7",
)
