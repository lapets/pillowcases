===========
pillowcases
===========

Library that makes it possible to work in a concise, algebraic way with Python Imaging Library image objects.

|pypi|

.. |pypi| image:: https://badge.fury.io/py/pillowcases.svg
   :target: https://badge.fury.io/py/pillowcases
   :alt: PyPI version and link.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/pillowcases>`__::

    python -m pip install pillowcases

The library can be imported in the usual way::

    import pillowcases

Examples
^^^^^^^^

To use this library, the ``PIL.Image`` module from the `pillow <https://pillow.readthedocs.io/en/stable>`__ library must be imported. If the ``pillowcases`` module is imported afterwards, the ``PIL.Image`` module's ``PIL.Image.Image`` class is redefined to refer to the ``pillowcases.Image`` class (which is itself derived from the ``PIL.Image.Image`` class).

    >>> import PIL.Image
    >>> import pillowcases
    >>> i = PIL.Image.frombytes('RGBA', (2, 2), bytes([0]*16))
    >>> isinstance(i, pillowcases.Image)
    True

.. |set| replace:: ``set``
.. _set: https://docs.python.org/3/library/stdtypes.html#set

.. |dict| replace:: ``dict``
.. _dict: https://docs.python.org/3/library/stdtypes.html#dict

Because instances of ``pillowcases.Image`` are `hashable <https://docs.python.org/3/glossary.html#term-hashable>`__, they can be added as elements to |set|_ objects and can be used as keys in |dict|_ objects.

    >>> j = PIL.Image.frombytes('RGBA', (2, 2), bytes([0]*16))
    >>> k = PIL.Image.frombytes('RGBA', (2, 2), bytes([255]*16))
    >>> len({i, j, k})
    2
    >>> d = {j: 1, k: 2}
    >>> d[k]
    2

Compare the above to the default behavior of the ``PIL.Image.Image`` class, demonstrated below.

    >>> from importlib import reload
    >>> PIL.Image = reload(PIL.Image)
    >>> i = PIL.Image.frombytes('RGBA', (2, 2), bytes([0]*16))
    >>> j = PIL.Image.frombytes('RGBA', (2, 2), bytes([0]*16))
    >>> j = PIL.Image.frombytes('RGBA', (2, 2), bytes([255]*16))
    >>> len({i, j, k})
    Traceback (most recent call last):
        ...
    TypeError: unhashable type: 'Image'

Testing
^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details)::

    python -m pip install .[test]
    python -m pytest

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/pillowcases>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/pillowcases>`__ by a package maintainer. First, install the dependencies required for packaging and publishing::

    python -m pip install .[publish]

Ensure that the correct version number appears in ``pyproject.toml``. Create and push a tag for this version (replacing ``?.?.?`` with the version number)::

    git tag ?.?.?
    git push origin ?.?.?

Remove any old build/distribution files. Then, package the source into a distribution archive::

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__::

    python -m twine upload dist/*
