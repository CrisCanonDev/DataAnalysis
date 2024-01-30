#Software divided into smaller programs (ease management)

# MODULE Unit independent from another unit
# Python file -> Module (Can contain classes, objects, functions)  

# Most common expressions:
    # -re
    # -math
    # -random
    # -os
    # -sys

import math    
print(math.cos(0))

#If needed to use module several times  
from math import cos
print(cos(1))


#MODULE LOOKUP
# 1) Check if it is a builtin module
# 2) Check if file mod.py found in any folders in list sys.path

# MODULE HIERARCHY
# Standard libraries contains hundred of modules.
# Python modules can be hierarchies into package
# Package -> Module contain other packages and modules



