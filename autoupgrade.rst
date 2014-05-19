Help on package autoupgrade:

NAME
    autoupgrade

FILE
    /home/jorgen/dev/autoupgrade/autoupgrade/__init__.py

PACKAGE CONTENTS
    version

CLASSES
    __builtin__.object
        AutoUpgrade
    exceptions.Exception(exceptions.BaseException)
        NoVersionsError
        PkgNotFoundError
    
    class AutoUpgrade(__builtin__.object)
     |  AutoUpgrade class, holds one package
     |  
     |  Methods defined here:
     |  
     |  __init__(self, pkg, index=None)
     |      Args:
     |      pkg (str): name of package
     |      index (str): alternative index, if not given https://pypi.python.org will be used
     |  
     |  check(self)
     |      Check if pkg has a later version
     |      Returns true if later version exists.
     |  
     |  restart(self)
     |      Restart application with same args as it was started.
     |      Does **not** return
     |  
     |  upgrade(self, dependencies=False)
     |      Upgrade the package unconditionaly
     |      Args:
     |          dependencies, update dependencies if True (see pip --no-deps)
     |  
     |  upgrade_if_needed(self, restart=True, dependencies=False)
     |      Upgrade the package if there is a later version available.
     |      Args:
     |          restart, restart app if True
     |          dependencies, update dependencies if True (see pip --no-deps)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class NoVersionsError(exceptions.Exception)
     |  No versions found for package
     |  
     |  Method resolution order:
     |      NoVersionsError
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __setstate__(...)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  __unicode__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |  
     |  __dict__
     |  
     |  args
     |  
     |  message
    
    class PkgNotFoundError(exceptions.Exception)
     |  No package found
     |  
     |  Method resolution order:
     |      PkgNotFoundError
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __setstate__(...)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  __unicode__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |  
     |  __dict__
     |  
     |  args
     |  
     |  message

FUNCTIONS
    normalize_version(v)
        Helper function to normalize version
        Returns a comparable object
        Args:
            v (str) version, e.g. "0.1.0"

DATA
    argv = ['/usr/lib/python2.7/pydoc.py', 'autoupgrade']
    environ = {'LC_NUMERIC': 'sv_SE.UTF-8', 'WINDOWID': '52428...re/:/usr/...
    executable = '/home/jorgen/dev/autoupgrade/venv/bin/python'


