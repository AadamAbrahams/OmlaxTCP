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




This Raspberry Pi-Python API provides functions for the configuration and operation of the Parallax 555-28027 PIR sensor and the Omron D6T-1A-02 temperature sensor. The data read from these modules may then be relayed via TCP protocols, from many clients to a single server, using a simplified rendition of the integrated Python Socket package.


* Free software: MIT license
* Documentation: https://omlaxtcp.readthedocs.io.


Features
-------

**Basic configuration and operation of:**
    * The Parallax 555-28027 PIR motion sensor (and potentially any PIR motion sensor, with a single output pin, that reads 1 for triggered and 0 for untriggered)
    * The Omron D6T-1A-02 temperature sensor using I2C communication protocols.
    * TCP network protocols using a simplified rendition of the integrated Python Socket package.
	
**Additional functionality includes:**
	* Speed detection through the use of two PIR motion sensors seperated by a specified distance. 
	* Direction detection through the use of two PIR motion sensors opposing one another, such that one is triggered prior to the other.
	* Fever detection through the use of a single temperature sensor and a given maximum temperature boundary. (Can be used to determine if anything produces a temperature above a given maximum, not specifically human temperatures.)
    
Hardware and Software Prerequisites
-------
A majority of the functions contained within this API may require a certain hardware module attached and/or a specific set of python libraries installed to operate as intended.

To make use of any of the functions contained in the motionSensor.py_ file, a Parallax 555-28027 PIR motion sensor is required. However, it would be possible to use any PIR motion sensor, with a single output pin, that outputs 1 when triggered and 0 while untriggered.   

.. _motionSensor.py: https://github.com/AadamAbrahams/OmlaxTCP/blob/master/omlaxtcp/motionSensor.py
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
