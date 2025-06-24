from setuptools import setup, find_packages
import os

# Dynamically load the version
version = {}
with open(os.path.join("lib_version", "__version__.py")) as f:
    exec(f.read(), version)

setup(
    name="lib_version",
    version=version["version"],
    description="A reusable Python library for retrieving its own version.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
