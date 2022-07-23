import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lush",
    version="0.9.1",
    author="Willem Pienaar",
    author_email="pypiorg@willem.co",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lush-dev/lush",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)