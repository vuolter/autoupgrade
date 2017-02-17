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

All the modules will be installed under the autoupgrade package, so **make sure
you have already removed the old [AutoUpgrade package]
(https://pypi.python.org/pypi/autoupgrade) before install this** to avoid an
installation conflict.


Usage
-----

### Classes

    class Package(__builtin__.object)

Basic package class, holds one package.

    class AutoUpgrade(__builtin__.object)

Legacy class refering to `Package` one.


### Methods

	__init__(self, pkg, index=None, verbose=False)

Arguments:
- `pkg` (str) name of package.
- `index` (str) alternative index, if not given default from *pip* will be used.
Include full index url, e.g. https://example.com/simple.

	check(self)

Decription: Check if `pkg` has a later version.
Returns true if later version exists.

	restart(self)

Decription: Restart application with same args as it was started.
Does NOT return.

	upgrade(self, dependencies=False, prerelease=False, force=False)

Decription: Upgrade the package unconditionaly.
Arguments:
- `dependencies` update dependencies if True _(see `pip --no-deps`)_.
- `prerelease` update to pre-release and development versions.
- `force` reinstall all packages even if they are already up-to-date.

	smartupgrade(self, restart=True, dependencies=False, prerelease=False)

Decription: Upgrade the package if there is a later version available.
Arguments:
- `restart` restart app if True.
- `dependencies` update dependencies if True _(see `pip --no-deps`)_.
- `prerelease` update to pre-release and development versions.

    upgrade_if_needed(self, restart=True, dependencies=False, prerelease=False)

Decription: Legacy method refering to `smartupgrade` one.


Release notes
-------------

- **0.3.0**
  - Fork of [autoupgrade](https://pypi.python.org/pypi/autoupgrade)
  - Python 3 support
  - Removed unnecessary dependencies
  - Prerelease and force-reinstall support
  - Massive code refactoring and cleaning
  - Updated README and LICENSE
  - New exception `PIPError` to handle pip errors
  - Main class renamed to `Package`
  - More verbose messages
  - Small code optimizations and improvements
- **0.2.0**
  - Issue #2, Index did not work when specified
  - Issue #3, Autoupgrade should not print to console (added verbose flag to
  keep backward compatibility
  - Issue #4, Support for pip > 0.6
- **0.1.5**
  - Issue #1, Extra index did not work for all servers.
- **0.1.4**
  - Fixed bug when version contains characters.
- **0.1.3**
  - Fixed vital fault in 0.1.2
- **0.1.2**
  - Setup file fixes
  - Removed verbose output as default
  - Return value fixed of upgrade()
- **0.1.1**
  - Dependencies updated
- **0.1.0**
  - Initial release
