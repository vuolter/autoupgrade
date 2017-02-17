AutoUpgrade
===========

Automatic upgrade of PyPI packages.


Quick Start
-----------

    from autoupgrade import Package
    Package(packagename).smartupgrade()

Example:

    from autoupgrade import Package
    Package('pip').smartupgrade()

The above will upgrade the Python package `pip` only if there is a new version
available on the PyPI.
The upgrade will be unattended and the python script will be restarted.

Old methods are still supported: you can accomplish the same task calling:

    from autoupgrade import AutoUpgrade
    AutoUpgrade('pip').upgrade_if_needed()


Installation
------------

    pip install autoupgrade-ng

All the modules will be installed under the _autoupgrade_ package, so **make
sure you have already removed the old [AutoUpgrade package]
(https://pypi.python.org/pypi/autoupgrade) before install this** to avoid an
installation conflict.


Usage
-----

### Classes

    class Package(__builtin__.object)

**Decription**: Basic package class, holds one package.

    class AutoUpgrade(__builtin__.object)

**Decription**: Legacy class refering to `Package` one.


### Methods

    __init__(self, pkg, index=None, verbose=False)

**Decription**: None.

**Arguments**:
- `pkg` (str) name of package.
- `index` (str) alternative index, if not given default from *pip* will be used.
Include full index url _(e.g. https://example.com/simple)_.

**Return**: None.

    check(self)

**Decription**: Check if `pkg` has a later version.

**Arguments**: None.

**Return**: True if later version exists, else False.

    restart(self)

**Decription**: Restart application with same args as it was started.

**Arguments**: None.

**Return**: None.

    upgrade(self, dependencies=False, prerelease=False, force=False)

**Decription**: Upgrade the package unconditionaly.

**Arguments**:
- `dependencies` update dependencies if True _(see `pip --no-deps`)_.
- `prerelease` update to pre-release and development versions.
- `force` reinstall all packages even if they are already up-to-date.

**Return**: None.

    smartupgrade(self, restart=True, dependencies=False, prerelease=False)

**Decription**: Upgrade the package if there is a later version available.

**Arguments**:
- `restart` restart app if True.
- `dependencies` update dependencies if True _(see `pip --no-deps`)_.
- `prerelease` update to pre-release and development versions.

**Return**: None.

    upgrade_if_needed(self, restart=True, dependencies=False, prerelease=False)

**Decription**: Legacy method refering to `smartupgrade` one.

**Arguments**: Same as `smartupgrade`.

**Return**: Same as `smartupgrade`.


Licensing
---------

Please refer to the included [LICENSE](/LICENSE.md) for the extended license.


----------------------------
###### © 2017 Walter Purcaro
