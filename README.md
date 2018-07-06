# conda-demo
Demo on how to create an anaconda package from scratch


So you’ve written some great code in python. Chances are there are more people in the programming community that could benefit from using your code! If you already have a github repository, you are already on the way to publishing your python code so that the open source community can benefit from your creation.

Creating a python library installable with pip or anaconda is easy!

Should I use pip or anaconda?
Does your code depend on packages that can’t be installed with pip? (cough, gdal)

If your code depends on a library that can only be installed with one of the conda channels or a user’s conda channel, then you should definitely shoot for having your package installable with anaconda and not pip.

	Many people choose to upload their code to pypi (pip) and then use that as the source for their anaconda package. Alternatively, you can use your github repo as the source, but I haven’t added that to this guide yet.


Steps to upload code to pypi:

File Hierarchy:
    /mypackage
      /mypackage
        __init__.py
