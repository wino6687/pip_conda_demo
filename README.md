# conda-demo
Demo on how to create an anaconda package from scratch


So you’ve written some great code in python. That's awesome! Chances are there are more people in the programming community that could benefit from using it. If you already have a public github repository, you are on the way to publishing your python code so that the open source community can benefit from your creation.

Creating a python library installable with pip or anaconda is easy!


## Starting Info and Questionsf:

### What are pip and conda?
In many ways, pip is the default package installer in python, while conda is an environment manager that aims to take pip's place and do more. If you already have an instance of python installed and you just want to install a common package or two, pip is the way to go. But pip really is lacking when it comes to managing and tracking external dependencies and accessing all of the available python packages out there.

An external dependency is code that a python package depends on that is not itself a python package. This can be a problem for pip, because everything built in pip has a setup.py setup file associated with it. But if you use HDF5 as a dependency, its source code does not have a setup.py file.



### Should I use pip or anaconda?

 - Does your code depend on packages that can’t be installed with pip or are not in python at all? (gdal or HDF5 for example)
    - If your code depends on a library that can only be installed with one of the conda channels or a user’s conda channel, then you should definitely shoot for having your package installable with conda and not pip.
    - You can double check this by creating a new environment with conda and attempting to install your dependencies with pip first and then conda. Or you can create a yaml file with all of your dependencies and test the channels by editing your ```.condarc``` file.

 - There is nothing wrong with building both, and either maintaining both, or choosing the one that suits your package best to maintain.

# Initial Steps for Pip and Conda:
#### 1. Organize your code into the proper file heirarchy
#### 2. Add your ```__init__.py``` files
#### 3. Add a ```LICENSE```, and a ```README.md``` if you don't already have them

***

### 1. File Hierarchy:
```
/mypackage
  /mypackage
    __init__.py
    mypackage.py
    /mysubpackage
      __init__.py
      mysubpackage.py
```

You can refer to this git repository to see the proper file structure. The example package is simply called 'conda-demo'.

### 2. ```__init__.py``` files
  - These files help python identify your python files as importable packages. They have very simple contents:
  ```
  name = 'mypackage'
  ```

### 3. Adding a ```LICENSE``` file  
The United States has pretty strict licensing laws, and any source code you plan to distribute must have a license associated with it.
  -  [This page on the python-guide is a helpful intro to licenses](http://docs.python-guide.org/en/latest/writing/license/)

Most python libraries use MIT or BSD licenses, which are open source licenses. These types of licenses are more permissive and are easier for a wider variety of potential users to use in their workflows, especially users in industry.

# Creating a pip installable package:

You should already have completed the initial steps above before starting this section. If you've made it this far, the rest is easy!

### Make your setup.py file

```
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="conda-demo",
    version="1.0.0",
    author="demo_author",
    author_email="conda-demo@email.com",
    description="A small demo package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wino6687/conda-demo",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

```

Your setup.py file is your buildscript for setuptools. It is essentially what holds the most basic information about your package and where pip can find the rest of it (in your git repo). Every time you update your package, you will change the version number in your ```setup.py``` file before uploading it to pypi.

### Create your Distribution Archive Files:

Before you begin, try a ```pip install setuptools wheel``` to make sure they are up to date

Make sure you are in the same directory as your ```setup.py``` file (main directory of project)

  ```python3 setup.py sdist bdist_wheel```
```
### Uploading your code to PyPi: Python Package Index

[Here is the PyPi Guide to Making pip Installable Code](https://packaging.python.org/tutorials/packaging-projects/)

Steps to Upload Code to PyPi:


***

# Creating a conda installable package:

Making conda packages is a bit more complex than making pip installable libraries. Conda is more powerful, but also a much larger and complex system.

### Initial Considerations:

##### What channel do I want to use to install my library?
- Default (Conda)
- [conda-forge](https://conda-forge.org)
- Personal channel

By default, [following the conda documentation](https://conda.io/docs/user-guide/tutorials/build-pkgs.html), you will create a package that is installable through your personal channel. This is okay and is still publicly available, however there is one major limitation:

### Dependencies will all need to be installable with the channels specified in the user's .condarc file

- If a user attempts to install your package, and it has dependencies from other user's private channels, conda-forge, or pip, they will first have to add all those channels to their ```.condarc``` file
- You have to be careful mixing dependency channels in your environment. Certain packages do not function properly if their dependencies are not all installed on the same channel.
  - If you have this issue, skip to the conda-forge section.


If you are building a package with the purpose of being used within other packages, meaning it will be a dependency for other people's work, then it makes more sense to publish with conda-forge. However, if your package is more of a 'top level' program that may have many dependencies but is not intended to be a dependency for other programs, then publishing in conda will do just fine! You can always decide to release on conda-forge in the future as well.










### conda-forge

[The conda-forge guide](https://github.com/conda-forge/staged-recipes) for creating packages is quite different from the default conda route.

conda-forge works a bit differently than normal conda. If you recall from above, mixing the channels that dependencies are downloaded with can create issues and prevent dependencies from being found. Conda-forge fixes this issue by requireing all of your package's dependencies to already be on the conda-forge or default channels.
