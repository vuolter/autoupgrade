autoupgrade
===========

Automatic upgrade of Python modules and packages

quick start
-----------

::

    :::python
    from autoupgrade import AutoUpgrade
    AutoUpgrade("pip").upgrade_if_needed()

The above will upgrade "pip" if there is a new version of pip out there.
The upgrade will be unattended and the python script will be restarted

installation
------------

::

    pip install autoupgrade

or install latest from repo:

::

    pip install https://bitbucket.org/jorkar/autoupgrade/get/master.tar.gz

api
---

classes
~~~~~~~

::

    :::python
    class AutoUpgrade(__builtin__.object)

AutoUpgrade class, holds one package

Methods
^^^^^^^

::

    :::python
    __init__(self, pkg, index=None)

Args: pkg (str): name of package index (str): alternative index, if not
given https://pypi.python.org will be used

::

    :::python
    check(self)

Check if pkg has a later version Returns true if later version exists.

::

    :::python
    restart(self)

Restart application with same args as it was started. Does **not**
return

::

    :::python
    upgrade(self, dependencies=False)

Upgrade the package unconditionaly Args: dependencies, update
dependencies if True (see pip--no-deps)

::

    :::python
    upgrade_if_needed(self, restart=True, dependencies=False)

Upgrade the package if there is a later version available. Args:
restart, restart app if True dependencies, update dependencies if True
(see pip --no-deps)

Supported platforms
-------------------

Currently tested on Linux with Python 2.7. Should be usable on Windows
and \*nix.

Test for Python 3 will be done some time.

Release notes
-------------

0.1.3
~~~~~

-  Fixed vital fault in 0.1.2

0.1.2
~~~~~

-  Setup file fixes
-  Removed verbose output as default
-  Return value fixed of upgrade()

0.1.1
~~~~~

-  Dependencies updated

0.1.0
~~~~~

Initial release

Info
====

-  Homepage: https://bitbucket.org/jorkar/autoupgrade

