print("""
# PACKAGES
# Packages are a way of structuring Python’s module namespace by using “dotted module names”
# Collection of modules (a “package”)
# Package structure
packages/
        __init__.py
        arithmetics/
                    __init__.py 
                    addition.py
                    subtract.py

# Importing in interactive terminal and using
from packages.arithmetic import addition
addition.sum(2,4)
6
from packages.arithmetic import subtract
subtract.minus(10,5)

""")