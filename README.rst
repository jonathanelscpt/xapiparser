========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.com/jonathanelscpt/xapiparser.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/jonathanelscpt/xapiparser

.. |codecov| image:: https://codecov.io/gh/jonathanelscpt/xapiparser/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/jonathanelscpt/xapiparser

.. |version| image:: https://img.shields.io/pypi/v/xapiparser.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/xapiparser

.. |wheel| image:: https://img.shields.io/pypi/wheel/xapiparser.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/xapiparser

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/xapiparser.svg
    :alt: Supported versions
    :target: https://pypi.org/project/xapiparser

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/xapiparser.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/xapiparser

.. |commits-since| image:: https://img.shields.io/github/commits-since/jonathanelscpt/xapiparser/v0.0.14.svg
    :alt: Commits since latest release
    :target: https://github.com/jonathanelscpt/xapiparser/compare/v0.0.14...master



.. end-badges

XAPI ssh command parser to convert cli commands to xml for use in the Cisco XAPI REST API

* Free software: MIT license

Installation
============

::

    pip install xapiparser

You can also install the in-development version with::

    pip install https://github.com/jonathanelscpt/xapiparser/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import xapiparser

    xapi = 'xConfiguration Conference Encryption Mode'
    xapiparser.parse(xapi)


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
