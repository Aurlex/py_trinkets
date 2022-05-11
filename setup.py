from setuptools import setup, find_packages

from py_trinkets import __version__

setup(
    name="py_trinkets",
    version=__version__,
    url="https://github.com/Aurlex/py_trinkets",
    author="Aurlex",
    author_email="aurlex1@gmail.com",
    packages=find_packages(),
    py_modules=find_packages(),
)
