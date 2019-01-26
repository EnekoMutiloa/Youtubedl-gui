#To create the .exe file for windows:

#pip3 install pyinstaller
#pyinstaller GUI.y

from distutils.core import setup
import py2exe
import sys

setup(
	windows=['GUI.py'],
)