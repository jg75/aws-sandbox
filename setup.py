from setuptools import setup, find_packages

setup(
    name="aws-sandbox",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "aws-cdk-lib",
    ],
)
