import re

from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


def get_version():
    init_py = open(os.path.join(os.path.dirname(__file__), 'vargur_sdk', '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version()


setup(
    name="vargur-sdk",
    version="0.1.3",
    author="MelonCafe",
    author_email="contact@siege-green.com",
    description="A powerful SDK for building extensible applications with plugin support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meloncafe/vargur-sdk",
    packages=find_packages(),
    install_requires=[
        "fastapi",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires='>=3.11',
    project_urls={
        "Bug Tracker": "https://github.com/meloncafe/vargur-sdk/issues",
        "Documentation": "https://vargur-sdk.siege-green.com/",
        "Source Code": "https://github.com/meloncafe/vargur-sdk",
    },
)