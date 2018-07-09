# conda-demo
Demo on how to create an anaconda package from scratch


So you’ve written some great code in python. That's great! Chances are there are more people in the programming community that could benefit from using it. If you already have a public github repository, you are already on the way to publishing your python code so that the open source community can benefit from your creation.

Creating a python library installable with pip or anaconda is easy!


## Starting Questions to ask yourself:

### Should I use pip or anaconda?
In many ways, pip and anaconda are not exactly competing directly against eachother. Each has a set of strengths and weaknesses. Put simply, pip is for managing python packages, and conda is for environment manangement. While these may sound very similar, there is a key distinction! If you already have an instance of python installed and you just want to install a package or two, pip is the way to go. But pip really is lacking when it comes to managing and tracking external dependencies.

An external dependency is code that a python package depends on that is not itself a python package. Numpy, for example, relies on packages built in C, rather than python. While it is possible to build a package like this in pip, conda will do more for you along the way to assist in the process.


#### First Question to ask yourself:
 - Does your code depend on packages that can’t be installed with pip? (gdal for example)

  - If your code depends on a library that can only be installed with one of the conda channels or a user’s conda channel, then you should definitely shoot for having your package installable with anaconda and not pip.


## PYPI: Python Package Index
Many people choose to upload their code to pypi (pip) and then use that as the source for their anaconda package. Alternatively, you can use your github repo as the source, but I haven’t added that to this guide yet.


Steps to upload code to pypi:

File Hierarchy
```
/mypackage
  /mypackage
    __init__.py
```
