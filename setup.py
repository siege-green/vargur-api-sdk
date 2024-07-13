from setuptools import setup, find_packages

setup(
    name="vargur-sdk",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
        ],
    },
)
