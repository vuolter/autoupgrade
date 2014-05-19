Help on package autoupgrade:

NAME  
autoupgrade

FILE  
/home/jorgen/dev/autoupgrade/autoupgrade/\_\_init\_\_.py

PACKAGE CONTENTS  
version

CLASSES  
\_\_builtin\_\_.object  
AutoUpgrade

exceptions.Exception(exceptions.BaseException)  
NoVersionsError PkgNotFoundError

class AutoUpgrade(\_\_builtin\_\_.object)  
 AutoUpgrade class, holds one package

 Methods defined here:

 \_\_init\_\_(self, pkg, index=None)  
     Args:  
     pkg (str): name of package  
     index (str): alternative index, if not given
<https://pypi.python.org> will be used

 check(self)  
     Check if pkg has a later version  
     Returns true if later version exists.

 restart(self)  
     Restart application with same args as it was started.  
     Does **not** return

 upgrade(self, dependencies=False)  
     Upgrade the package unconditionaly  
     Args:  
         dependencies, update dependencies if True (see pip --no-deps)

 upgrade\_if\_needed(self, restart=True, dependencies=False)  
     Upgrade the package if there is a later version available.  
     Args:  
         restart, restart app if True  
         dependencies, update dependencies if True (see pip --no-deps)

 ----------------------------------------------------------------------  
 Data descriptors defined here:

 \_\_dict\_\_  
     dictionary for instance variables (if defined)

 \_\_weakref\_\_  
     list of weak references to the object (if defined)

class NoVersionsError(exceptions.Exception)  
 No versions found for package

 Method resolution order:  
     NoVersionsError  
     exceptions.Exception  
     exceptions.BaseException  
     \_\_builtin\_\_.object

 Data descriptors defined here:

 \_\_weakref\_\_  
     list of weak references to the object (if defined)

 ----------------------------------------------------------------------  
 Methods inherited from exceptions.Exception:

 \_\_init\_\_(...)  
     x.\_\_init\_\_(...) initializes x; see help(type(x)) for signature

 ----------------------------------------------------------------------  
 Data and other attributes inherited from exceptions.Exception:

 \_\_new\_\_ = \<built-in method \_\_new\_\_ of type object\>  
     T.\_\_new\_\_(S, ...) -\> a new object with type S, a subtype of T

 ----------------------------------------------------------------------  
 Methods inherited from exceptions.BaseException:

 \_\_delattr\_\_(...)  
     x.\_\_delattr\_\_('name') \<==\> del x.name

 \_\_getattribute\_\_(...)  
     x.\_\_getattribute\_\_('name') \<==\> x.name

 \_\_getitem\_\_(...)  
     x.\_\_getitem\_\_(y) \<==\> x[y]

 \_\_getslice\_\_(...)  
     x.\_\_getslice\_\_(i, j) \<==\> x[i:j]

     Use of negative indices is not supported.

 \_\_reduce\_\_(...)

 \_\_repr\_\_(...)  
     x.\_\_repr\_\_() \<==\> repr(x)

 \_\_setattr\_\_(...)  
     x.\_\_setattr\_\_('name', value) \<==\> x.name = value

 \_\_setstate\_\_(...)

 \_\_str\_\_(...)  
     x.\_\_str\_\_() \<==\> str(x)

 \_\_unicode\_\_(...)

 ----------------------------------------------------------------------  
 Data descriptors inherited from exceptions.BaseException:

 \_\_dict\_\_

 args

 message

class PkgNotFoundError(exceptions.Exception)  
 No package found

 Method resolution order:  
     PkgNotFoundError  
     exceptions.Exception  
     exceptions.BaseException  
     \_\_builtin\_\_.object

 Data descriptors defined here:

 \_\_weakref\_\_  
     list of weak references to the object (if defined)

 ----------------------------------------------------------------------  
 Methods inherited from exceptions.Exception:

 \_\_init\_\_(...)  
     x.\_\_init\_\_(...) initializes x; see help(type(x)) for signature

 ----------------------------------------------------------------------  
 Data and other attributes inherited from exceptions.Exception:

 \_\_new\_\_ = \<built-in method \_\_new\_\_ of type object\>  
     T.\_\_new\_\_(S, ...) -\> a new object with type S, a subtype of T

 ----------------------------------------------------------------------  
 Methods inherited from exceptions.BaseException:

 \_\_delattr\_\_(...)  
     x.\_\_delattr\_\_('name') \<==\> del x.name

 \_\_getattribute\_\_(...)  
     x.\_\_getattribute\_\_('name') \<==\> x.name

 \_\_getitem\_\_(...)  
     x.\_\_getitem\_\_(y) \<==\> x[y]

 \_\_getslice\_\_(...)  
     x.\_\_getslice\_\_(i, j) \<==\> x[i:j]

     Use of negative indices is not supported.

 \_\_reduce\_\_(...)

 \_\_repr\_\_(...)  
     x.\_\_repr\_\_() \<==\> repr(x)

 \_\_setattr\_\_(...)  
     x.\_\_setattr\_\_('name', value) \<==\> x.name = value

 \_\_setstate\_\_(...)

 \_\_str\_\_(...)  
     x.\_\_str\_\_() \<==\> str(x)

 \_\_unicode\_\_(...)

 ----------------------------------------------------------------------  
 Data descriptors inherited from exceptions.BaseException:

 \_\_dict\_\_

 args

 message

FUNCTIONS  
normalize\_version(v)  
Helper function to normalize version Returns a comparable object Args: v
(str) version, e.g. "0.1.0"

DATA  
argv = ['/usr/lib/python2.7/pydoc.py', 'autoupgrade'] environ =
{'LC\_NUMERIC': 'sv\_SE.UTF-8', 'WINDOWID': '52428...re/:/usr/...
executable = '/home/jorgen/dev/autoupgrade/venv/bin/python'


