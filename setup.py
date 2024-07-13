from setuptools import setup, find_packages

setup(
    name="vargur_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "aioredis",
        "pyjwt",
        "discord.py",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
        ],
    },
)
