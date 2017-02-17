AutoUpgrade
===========

.. image:: https://img.shields.io/pypi/v/autoupgrade-ng.svg
   :target: https://pypi.python.org/pypi/autoupgrade-ng

.. image:: https://img.shields.io/github/issues/vuolter/autoupgrade.svg
   :target: https://github.com/vuolter/autoupgrade/issues

.. image:: https://img.shields.io/pypi/dm/autoupgrade-ng.svg
   :target: https://pypi.python.org/pypi/autoupgrade-ng

.. image:: https://img.shields.io/pypi/l/autoupgrade-ng.svg
   :target: https://pypi.python.org/pypi/autoupgrade-ng

.. image:: https://img.shields.io/pypi/format/autoupgrade-ng.svg
   :target: https://pypi.python.org/pypi/autoupgrade-ng

.. image:: https://img.shields.io/pypi/pyversions/autoupgrade-ng.svg
   :target: https://pypi.python.org/pypi/autoupgrade-ng

.. image:: https://img.shields.io/pypi/status/autoupgrade-ng.svg
   :target: https://pypi.python.org/pypi/autoupgrade-ng

.. image:: https://img.shields.io/twitter/url/https/twitter.com/WalterPurcaro.svg?style=social
   :target: https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D

.. image:: https://img.shields.io/github/stars/vuolter/autoupgrade.svg
   :target: https://github.com/vuolter/autoupgrade/stargazers


Quick Start
-----------

::

    from autoupgrade import Package
    Package(<packagename>).smartupgrade()

Example:

::

    from autoupgrade import Package
    Package('pip').smartupgrade()

The above will upgrade the Python package ``pip`` only if there is a new version
available on the PyPI.
The upgrade will be unattended and the python script will be restarted.

Old methods are still supported; you can accomplish the same task calling:

::

    from autoupgrade import AutoUpgrade
    AutoUpgrade('pip').upgrade_if_needed()


Installation
------------

::

    pip install autoupgrade-ng

All the modules will be installed under the *autoupgrade* package, so **make
sure you have already removed the old AutoUpgrade package
(https://pypi.python.org/pypi/autoupgrade) before install this** to avoid an
installation conflict.


Usage
-----

Classes
~~~~~~~

::

    class Package(__builtin__.object)

**Decription**: Basic package class, holds one package.

::

    class AutoUpgrade(__builtin__.object)

**Decription**: Legacy class refering to ``Package`` one.

Methods
~~~~~~~

::

    __init__(self, pkg, index=None, verbose=False)

**Decription**: None.

**Arguments**:

-  ``pkg`` (str) name of package.
-  | ``index`` (str) alternative index, if not given default from *pip*
     will be used.
   | Include full index url \_(e.g. \ https://example.com/simple)_.
   | **Return**: None.

::

   check(self)

**Decription**: Check if ``pkg`` has a later version.

**Arguments**: None.

**Return**: True if later version exists, else False.

::

    restart(self)

**Decription**: Restart application with same args as it was started.

**Arguments**: None.

**Return**: None.

::

    upgrade(self, dependencies=False, prerelease=False, force=False)

**Decription**: Upgrade the package unconditionaly.

**Arguments**:

-  ``dependencies`` update dependencies if True *(see
   ``pip --no-deps``)*.
-  ``prerelease`` update to pre-release and development versions.
-  | ``force`` reinstall all packages even if they are already
     up-to-date.

**Return**: None.

::

   smartupgrade(self, restart=True, dependencies=False,
   prerelease=False)

**Decription**: Upgrade the package if there is a later version available.

**Arguments**:

-  ``restart`` restart app if True.
-  ``dependencies`` update dependencies if True *(see
   ``pip --no-deps``)*.
-  | ``prerelease`` update to pre-release and development versions.

**Return**: None.

::

   upgrade\_if\_needed(self, restart=True, dependencies=False,
   prerelease=False)

**Decription**: Legacy method refering to ``smartupgrade`` one.

**Arguments**: Same as ``smartupgrade``.

**Return**: Same as ``smartupgrade``.


Release notes
-------------

**0.3.0**:

-  Fork of autoupgrade (https://pypi.python.org/pypi/autoupgrade).
-  Python 3 support.
-  Removed unnecessary dependencies.
-  Pre-release and force-reinstall support.
-  Massive code refactoring and cleaning.
-  Updated README and LICENSE.
-  New exception ``PIPError`` to handle pip errors.
-  Main class renamed to ``Package``.
-  More verbose messages.
-  Small code optimizations and improvements.

**0.2.0**:

-  Issue #2, Index did not work when specified.
-  Issue #3, Autoupgrade should not print to console (added verbose flag
   to
   keep backward compatibility.
-  Issue #4, Support for pip > v0.6 .

**0.1.5**:

-  Issue #1, Extra index did not work for all servers.

**0.1.4**:

-  Fixed bug when version contains characters.

**0.1.3**:

-  Fixed vital fault in v0.1.2 .

**0.1.2**:

-  Setup file fixes
-  Removed verbose output as default.
-  Return value fixed of method ``upgrade``.

**0.1.1**:

-  Dependencies updated.

**0.1.0**:

-  Initial release.
