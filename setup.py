import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pip_conda_demo",
    version="0.0.1",
    author="William Norris",
    author_email="wino6687@colorado.edu",
    description="A python package for demonstrating how to make pip and conda libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wino6687/pip_conda_demo",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ),
)
