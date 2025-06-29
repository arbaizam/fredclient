from setuptools import setup, find_packages

setup(
    name="fredclient",
    version="0.1.0",
    author="arbaizam",
    description="A lightweight Python wrapper for the FRED API",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
)