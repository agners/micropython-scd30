import sys
sys.path.pop(0)
from setuptools import setup
from codecs import open
from os import path

cwd = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="micropython-scd30",
    py_modules=["scd30"],
    version="0.1.0",
    description="MicroPython I2C driver for SCD30 CO2 sensor module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="scd30, co2, temperature, humidity, micropython, i2c",
    url="https://github.com/agners/micropython-scd30",
    author="Stefan Agner",
    author_email="stefan@agner.ch",
    maintainer="Stefan Agner",
    maintainer_email="stefan@agner.ch",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
