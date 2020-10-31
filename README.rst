========
OmlaxTCP
========


.. image:: https://img.shields.io/pypi/v/omlaxtcp.svg
        :target: https://pypi.python.org/pypi/omlaxtcp

.. image:: https://img.shields.io/travis/AadamAbrahams/omlaxtcp.svg
        :target: https://travis-ci.com/AadamAbrahams/omlaxtcp

.. image:: https://readthedocs.org/projects/omlaxtcp/badge/?version=latest
        :target: https://omlaxtcp.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




This API provides functions for the configuration and operation of the Parallax 555-28027 PIR sensor and the Omron D6T-1A-02 temperature sensor. The data read from these modules may then be relayed via TCP protocols, from many clients to a single server, using a simplified rendition of the integrated Python Socket package.


* Free software: MIT license
* Documentation: https://omlaxtcp.readthedocs.io.


Features
--------
Basic configuration and operation of:
    * The Parallax 555-28027 PIR motion sensor (and potentially any PIR motion sensor, with a single output pin, that reads 1 for high and 0 for low)
    * The Omron D6T-1A-02 temperature sensor using I2C communication protocols.
    * TCP network protocols using a simplified rendition of the integrated Python Socket package.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
