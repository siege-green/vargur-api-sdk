from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="vargur-sdk",
    version="0.1.2",
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
)