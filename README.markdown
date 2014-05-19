# autoupgrade

Automatic upgrade of Python modules and packages

## quick start

	from autoupgrade import AutoUpgrade
    	AutoUpgrade("pip").upgrade_if_needed()
The above will upgrade "pip" if there is a new version of pip out there. 
The upgrade will be unattended and the pyuthon script will be restarted

## installation

	pip install autoupgrade

## api

### AutoUpgrade

AutoUpgrade is the only class in the moment. Pulbic methods:

	upgrade_if_needed(self, restart = True, dependencies = False)

Upgrade automatically the package if needed. Flags for restart and wether dependencises shall be installed is available.

	upgrade(self, dependencies = False)

upgrade always /you should run check prior to this)

	restart(self)

restart always

	check(self)

returns true if autoupdate finds a newer version

## Supported platforms

Currently tested on Linux with Python 2.7.
Should be usable on Windows and *nix.

Test for Python 3 will be done some time.


#Release notes

##0.1.0
Initial release

#### 
# Info

- Homepage: https://bitbucket.org/jorkar/autoupgrade
