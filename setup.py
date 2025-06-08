from setuptools import setup, find_packages
from lib_version.version import __version__

setup(
    name="lib-version",
    version=__version__,
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    description="Lightweight version utility for reuse in REMLA services",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
