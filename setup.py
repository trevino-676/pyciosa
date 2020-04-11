import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyciosa",
    version="0.0.1",
    author="Marco A. Gallegos",
    author_email="ma_galeza@hotmail.com",
    description="common utilities for new projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marco-gallegos/pyciosa.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)