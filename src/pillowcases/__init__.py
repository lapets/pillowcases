"""Allow users to access the derived class and modify the ``PIL`` module."""
import PIL.Image
from pillowcases.pillowcases import Image

PIL.Image.Image = Image # Replace class definition with that of derived class.
