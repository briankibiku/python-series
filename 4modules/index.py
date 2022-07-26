print("""
# MODULES
# split it into several files for easier maintenance. 
# A handy function that you'd want to reuse in several programs without copying its definition into each program.
# Putting definitions in a file and using them in a script or in an interactive instance of the interpreter.
# Such a file is called a MODULE
# A module is a file containing Python definitions and statements.

# Create a file with name (addition)
# Add a sum function

#USING a module
# Import by name
from addition import sum    
print(sum(2,3))

# import all names/functions
from fibo import *
#If the module name is followed by as, then the name following as is bound directly to the imported module
import addition as add
importlib.reload(), 

# STANDARD MODULES
# Python comes with a library of standard modules
# The dir() function # used to find out which names a module defines
>>> import math
>>> dir(math)
>>> import builtins
>>> dir(builtins) 

# PACKAGES
# Packages are a way of structuring Python’s module namespace by using “dotted module names”
# Collection of modules (a “package”)

""")    