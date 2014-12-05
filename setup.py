"""
AUTHOR: Nelson Dos Santos
CREATION: 5.12.2014

USE THIS JUST TO BUILT THE APPLICATION!

Setup file to build the scripts of this application to create an .app
This scripts uses py2app library, so make sure you have it.

To build the application again, you should type this command:

                  python3 setup.py py2app
"""

from setuptools import setup



# main script
APP = ['source/main.py']

# other files

DATA_FILES = [('', ['source/sounds']), ('', ['source/__pycache__'])]

OPTIONS ={}

setup(
    app = APP,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app']
)
