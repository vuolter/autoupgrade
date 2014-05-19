  ----------------- -----------------------------------------------------------------------------------------------------------------------
   \                [index](.)\
    \               [/home/jorgen/dev/autoupgrade/autoupgrade/\_\_init\_\_.py](file:/home/jorgen/dev/autoupgrade/autoupgrade/__init__.py)
  **autoupgrade**   
  ----------------- -----------------------------------------------------------------------------------------------------------------------

 \
 **Package Contents**

`      `

 

  -------------------------------------- -- -- --
  [version](autoupgrade.version.html)\         
                                               
  -------------------------------------- -- -- --

 \
 **Classes**

`      `

 

[\_\_builtin\_\_.object](__builtin__.html#object)

[AutoUpgrade](autoupgrade.html#AutoUpgrade)

[exceptions.Exception](exceptions.html#Exception)([exceptions.BaseException](exceptions.html#BaseException))

[NoVersionsError](autoupgrade.html#NoVersionsError)

[PkgNotFoundError](autoupgrade.html#PkgNotFoundError)

 \
 class
**AutoUpgrade**([\_\_builtin\_\_.object](__builtin__.html#object))

`   `

`AutoUpgrade class, holds one package `

 

Methods defined here:\

**\_\_init\_\_**(self, pkg, index=None)
:   `Args: pkg (str): name of package index (str): alternative index, if not given https://pypi.python.org will be used`

**check**(self)
:   `Check if pkg has a later version Returns true if later version exists.`

**restart**(self)
:   `Restart application with same args as it was started. Does **not** return`

**upgrade**(self, dependencies=False)
:   `Upgrade the package unconditionaly Args:     dependencies, update dependencies if True (see pip --no-deps)`

**upgrade\_if\_needed**(self, restart=True, dependencies=False)
:   `Upgrade the package if there is a later version available. Args:     restart, restart app if True     dependencies, update dependencies if True (see pip --no-deps)`

* * * * *

Data descriptors defined here:\

**\_\_dict\_\_**
:   `dictionary for instance variables (if defined)`

**\_\_weakref\_\_**
:   `list of weak references to the object (if defined)`

 \
 class
**NoVersionsError**([exceptions.Exception](exceptions.html#Exception))

`   `

`No versions found for package `

 

Method resolution order:
:   [NoVersionsError](autoupgrade.html#NoVersionsError)
:   [exceptions.Exception](exceptions.html#Exception)
:   [exceptions.BaseException](exceptions.html#BaseException)
:   [\_\_builtin\_\_.object](__builtin__.html#object)

* * * * *

Data descriptors defined here:\

**\_\_weakref\_\_**
:   `list of weak references to the object (if defined)`

* * * * *

Methods inherited from
[exceptions.Exception](exceptions.html#Exception):\

**\_\_init\_\_**(...)
:   `x.__init__(...) initializes x; see help(type(x)) for signature`

* * * * *

Data and other attributes inherited from
[exceptions.Exception](exceptions.html#Exception):\

**\_\_new\_\_** = \<built-in method \_\_new\_\_ of type object\>

`T.__new__(S, ...) -> a new object with type S, a subtype of T`

* * * * *

Methods inherited from
[exceptions.BaseException](exceptions.html#BaseException):\

**\_\_delattr\_\_**(...)
:   `x.__delattr__('name') <==> del x.name`

**\_\_getattribute\_\_**(...)
:   `x.__getattribute__('name') <==> x.name`

**\_\_getitem\_\_**(...)
:   `x.__getitem__(y) <==> x[y]`

**\_\_getslice\_\_**(...)
:   `x.__getslice__(i, j) <==> x[i:j]   Use of negative indices is not supported.`

**\_\_reduce\_\_**(...)

**\_\_repr\_\_**(...)
:   `x.__repr__() <==> repr(x)`

**\_\_setattr\_\_**(...)
:   `x.__setattr__('name', value) <==> x.name = value`

**\_\_setstate\_\_**(...)

**\_\_str\_\_**(...)
:   `x.__str__() <==> str(x)`

**\_\_unicode\_\_**(...)

* * * * *

Data descriptors inherited from
[exceptions.BaseException](exceptions.html#BaseException):\

**\_\_dict\_\_**

**args**

**message**

 \
 class
**PkgNotFoundError**([exceptions.Exception](exceptions.html#Exception))

`   `

`No package found `

 

Method resolution order:
:   [PkgNotFoundError](autoupgrade.html#PkgNotFoundError)
:   [exceptions.Exception](exceptions.html#Exception)
:   [exceptions.BaseException](exceptions.html#BaseException)
:   [\_\_builtin\_\_.object](__builtin__.html#object)

* * * * *

Data descriptors defined here:\

**\_\_weakref\_\_**
:   `list of weak references to the object (if defined)`

* * * * *

Methods inherited from
[exceptions.Exception](exceptions.html#Exception):\

**\_\_init\_\_**(...)
:   `x.__init__(...) initializes x; see help(type(x)) for signature`

* * * * *

Data and other attributes inherited from
[exceptions.Exception](exceptions.html#Exception):\

**\_\_new\_\_** = \<built-in method \_\_new\_\_ of type object\>

`T.__new__(S, ...) -> a new object with type S, a subtype of T`

* * * * *

Methods inherited from
[exceptions.BaseException](exceptions.html#BaseException):\

**\_\_delattr\_\_**(...)
:   `x.__delattr__('name') <==> del x.name`

**\_\_getattribute\_\_**(...)
:   `x.__getattribute__('name') <==> x.name`

**\_\_getitem\_\_**(...)
:   `x.__getitem__(y) <==> x[y]`

**\_\_getslice\_\_**(...)
:   `x.__getslice__(i, j) <==> x[i:j]   Use of negative indices is not supported.`

**\_\_reduce\_\_**(...)

**\_\_repr\_\_**(...)
:   `x.__repr__() <==> repr(x)`

**\_\_setattr\_\_**(...)
:   `x.__setattr__('name', value) <==> x.name = value`

**\_\_setstate\_\_**(...)

**\_\_str\_\_**(...)
:   `x.__str__() <==> str(x)`

**\_\_unicode\_\_**(...)

* * * * *

Data descriptors inherited from
[exceptions.BaseException](exceptions.html#BaseException):\

**\_\_dict\_\_**

**args**

**message**

 \
 **Functions**

`      `

 

**normalize\_version**(v)
:   `Helper function to normalize version Returns a comparable object Args:     v (str) version, e.g. "0.1.0"`

  ----------- --- -------------------------------------------------------------------------------------------------------------------------
   \
   **Data**

  `      `        **argv** = ['/usr/lib/python2.7/pydoc.py', '-w', 'autoupgrade']\
                   **environ** = {'LC\_NUMERIC': 'sv\_SE.UTF-8', 'WINDOWID': '52428...re/:/usr/share/:/usr/share', 'XDG\_SEAT': 'seat0'}\
                   **executable** = '/home/jorgen/dev/autoupgrade/venv/bin/python'
  ----------- --- -------------------------------------------------------------------------------------------------------------------------


