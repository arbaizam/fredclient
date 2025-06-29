
from setuptools import setup, find_packages

setup(
    name="fredclient",
    version="0.1.0",
    description="Python client for the FRED API",
    author="arbaizam",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
