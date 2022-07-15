"""Gives users access to derived class and modifies ``PIL`` module."""
import PIL.Image
from pillowcases.pillowcases import Image

PIL.Image.Image = Image # Replace class definition with derived class.
