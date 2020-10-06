
# How to Publish a Pip or Conda library (Companion Repo to [Earth Lab blog post](https://www.colorado.edu/earthlab/2019/01/03/publishing-your-python-code-pip-and-conda-tips-and-best-practices))

### Should I use pip, conda, or conda-forge?

 - There is no one answer to this question. There are plenty of people that prefer pip and plenty others who prefer conda. While conda may be better suited for certain more complex packages, there is a growing population of the python community that is moving back to pip from conda. Pip has that lovely simplicity that many people love about Python. However, there is one particular reason you would want to use conda:

 - Does your code depend on packages that can’t be installed with pip or are not in python at all? (gdal or HDF5 for example)
    - If your code depends on a library that can only be installed with one of the conda channels or a user’s conda channel, then you should definitely shoot for having your package installable with conda and not pip.
    - You can double check this by creating a new environment with conda and attempting to install your dependencies with pip first and then conda. Or you can create a yaml file with all of your dependencies and test the channels by editing your ```.condarc``` file.
      - If you depend on pacakages from conda, and you intend to have your library be a dependency within other's code, then using the conda-forge channel makes the most sense.

  There is nothing wrong with building both, and either maintaining both, or choosing the one that suits your package best to maintain. Most of my personal libraries I publish on both pypi (pip) and conda-forge. I really enjoy the extra level of quality that conda-forge ensures, which I will discuss below.  

# Initial Steps for Pip and Conda:
#### 1. Organize your code into the proper file heirarchy
#### 2. Add your ```__init__.py``` files
#### 3. Add a ```LICENSE```, and a ```README.md``` if you don't already have them

***

#### 1. File Hierarchy:
```
/mypackage
  /mypackage
    __init__.py
    mypackage.py
    /mysubpackage
      __init__.py
      mysubpackage.py
```

You can refer to this git repository to see the proper file structure. The example package is simply called ```pip_conda_demo``` and has a sub package called ```hello_world```.

#### 2. ```__init__.py``` files
  - These files help python identify your python files as importable packages. They have very simple contents:
  ```
  name = 'mypackage'
  ```

#### 3. Adding a ```LICENSE``` file
The United States has pretty strict licensing laws, and any source code you plan to distribute must have a license associated with it.
  -  [This page on the python-guide is a helpful intro to licenses](http://docs.python-guide.org/en/latest/writing/license/)

Most python libraries use MIT or BSD licenses, which are open source licenses. These types of licenses are more permissive and are easier for a wider variety of potential users to use in their workflows, especially users in industry.

Now that you have completed the steps above, you are ready to build a package for your preferred channel. The first section guides you to making a pip installable library, the next section is for conda, and then the last section covers conda-forge.

# Creating a pip installable package:

You should already have completed the initial steps above before starting this section. If you've made it this far, the rest is easy!

### 1. Make an account at pypi.org

### 2. Make your setup.py file

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

For a full list of possible classifiers to be used in your setup.py file, refer to [this link on PyPi's Docs](https://pypi.org/pypi?%3Aaction=list_classifiers)

### 3. Create your Distribution Archive Files:

Before you begin, try a ```python3 -m pip install --user --upgrade setuptools wheel``` to make sure they are up to date

Make sure you are in the same directory as your ```setup.py``` file (main directory of project)

  ```python3 setup.py sdist bdist_wheel```

This should create a ```dist``` folder in your main directory with the compressed files for your package!

### 4. Upload your distribution archives to pypi:
Check that you have twine installed:
```python3 -m pip install --user --upgrade twine```
Twine simply manages the file upload to PyPi. Next run this command:

```twine upload dist/*```
When you don't pass a location for twine to upload you distribution archives, it will default to the PyPi legacy servers, which is where we want your code!

You will be prompted for your PyPi login credentials, and then the upload will begin. Now you should be able to login to your account at pypi.org where you will be able to see your package.

### 5. Test you New Package
Wait 5-10 minutes for your uploaded package to be registered by pip. Sometimes you can install it right away, and other times it takes a few minutes.

```pip install conda-demo```

If you have further questions, [here is the PyPi Guide to Making pip Installable Code](https://packaging.python.org/tutorials/packaging-projects/)

### Pip Troubleshooting:
  - If you have trouble with twine not being found, try creating a conda environment and installing twine there:
    - ```conda create -n twine_env python=3.6 twine```
    - ```source activate twine_env```
    - ```twine upload dist/*```


***
## Maintaining a pip package:

Everytime you make a major improvement to your code, you will want to repeat this process and upload the new version to PyPi.org.

### Key Steps:
1. Change the version number in your setup.py file
2. Remove your old distribution archive files
3. In your package's main directory run: ```python3 setup.py sdist bdist_wheel``` to create new distribution archives
4. Upload this new version to PyPi: ```twine upload dist/*```

***


# Creating a conda installable package:

Making conda packages is a bit more complex than making pip installable libraries. Conda is more powerful, but also a much larger and complex system.

### Initial Considerations:

##### What channel do I want to use to install my library?
- Default (Conda)
- [conda-forge](https://conda-forge.org)
- Personal channel

By default, [following the conda documentation](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/building-conda-packages.html), you will create a package that is installable through your personal channel. This is okay and is still publicly available, however there is one major limitation:

### Dependencies will all need to be installable with the channels specified in the user's .condarc file

- If a user attempts to install your package, and it has dependencies from other user's private channels, conda-forge, or pip, they will first have to add all those channels to their ```.condarc``` file
- You have to be careful mixing dependency channels in your environment. Certain packages do not function properly if their dependencies are not all installed on the same channel.
  - If you have this issue, skip to the conda-forge section.


If you are building a package with the purpose of being used within other packages, meaning it will be a dependency for other people's work, then it makes more sense to publish with conda-forge. However, if your package is more of a 'top level' program that may have many dependencies but is not intended to be a dependency for other programs, then publishing in conda will do just fine! You can always decide to release on conda-forge in the future as well.










### conda-forge

[The conda-forge guide](https://github.com/conda-forge/staged-recipes) for creating packages is quite different from the default conda route.

conda-forge works a bit differently than normal conda. If you recall from above, mixing the channels that dependencies are downloaded with can create issues and prevent dependencies from being found. Conda-forge fixes this issue by requireing all of your package's dependencies to already be on the conda-forge or default channels.
