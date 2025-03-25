from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pyurlextract',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Deadpool2000',
    author_email='d2kyt@protonmail.com',
    description='A library to expand Short URL with all possible redirections',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Deadpool2000/pyurlextract",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)