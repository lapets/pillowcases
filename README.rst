===========
pillowcases
===========

Library that makes it possible to work in a concise, algebraic way with Python Imaging Library image objects.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/pillowcases.svg
   :target: https://badge.fury.io/py/pillowcases
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/pillowcases/badge/?version=latest
   :target: https://pillowcases.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/lapets/pillowcases/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/lapets/pillowcases/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/pillowcases/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/pillowcases?branch=main
   :alt: Coveralls test coverage summary.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/pillowcases>`__:

.. code-block:: bash

    python -m pip install pillowcases

The library can be imported in the usual way:

.. code-block:: python

    import pillowcases

Examples
^^^^^^^^

To use this library, the ``PIL.Image`` module from the `pillow <https://pillow.readthedocs.io/en/stable>`__ library must be imported. If the ``pillowcases`` module is imported afterwards, the ``PIL.Image`` module's ``PIL.Image.Image`` class is redefined to refer to the ``pillowcases.Image`` class (which is itself derived from the ``PIL.Image.Image`` class):

.. code-block:: python

    >>> import PIL.Image
    >>> import pillowcases
    >>> i = PIL.Image.frombytes('RGBA', (2, 2), bytes([0]*16))
    >>> isinstance(i, pillowcases.Image)
    True

.. |set| replace:: ``set``
.. _set: https://docs.python.org/3/library/stdtypes.html#set

.. |dict| replace:: ``dict``
.. _dict: https://docs.python.org/3/library/stdtypes.html#dict

Because instances of ``pillowcases.Image`` are `hashable <https://docs.python.org/3/glossary.html#term-hashable>`__, they can be added as elements to |set|_ objects and can be used as keys in |dict|_ objects:

.. code-block:: python

    >>> j = PIL.Image.frombytes('RGBA', (2, 2), bytes([0]*16))
    >>> k = PIL.Image.frombytes('RGBA', (2, 2), bytes([255]*16))
    >>> len({i, j, k})
    2
    >>> d = {j: 1, k: 2}
    >>> d[k]
    2

Compare the above to the default behavior of the ``PIL.Image.Image`` class, demonstrated below:

.. code-block:: python

    >>> from importlib import reload
    >>> PIL.Image = reload(PIL.Image)
    >>> i = PIL.Image.frombytes('RGBA', (2, 2), bytes([0]*16))
    >>> j = PIL.Image.frombytes('RGBA', (2, 2), bytes([0]*16))
    >>> j = PIL.Image.frombytes('RGBA', (2, 2), bytes([255]*16))
    >>> len({i, j, k})
    Traceback (most recent call last):
        ...
    TypeError: unhashable type: 'Image'

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__:

.. code-block:: bash

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__:

.. code-block:: bash

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details):

.. code-block:: bash

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__:

.. code-block:: bash

    python src/pillowcases/pillowcases.py -v

Style conventions are enforced using `Pylint <https://pylint.readthedocs.io>`__:

.. code-block:: bash

    python -m pip install .[lint]
    python -m pylint src/pillowcases

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/pillowcases>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/pillowcases>`__ by a package maintainer. First, install the dependencies required for packaging and publishing:

.. code-block:: bash

    python -m pip install .[publish]

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document to the Read the Docs documentation of this package (or its dependencies) have appropriate version numbers. Also ensure that the Read the Docs project for this library has an `automation rule <https://docs.readthedocs.io/en/stable/automation-rules.html>`__ that activates and sets as the default all tagged versions. Create and push a tag for this version (replacing ``?.?.?`` with the version number):

.. code-block:: bash

    git tag ?.?.?
    git push origin ?.?.?

Remove any old build/distribution files. Then, package the source into a distribution archive:

.. code-block:: bash

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__:

.. code-block:: bash

    python -m twine upload dist/*
