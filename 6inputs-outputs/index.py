print("""
# INPUT AND OUTPUT

# Output Formatting
# three ways of writing values: expression statements and the print() function and a third way is using the write() method of FILE objects

# There are several ways to format output.
# 1. use formatted string literals begin a string with f or F before the opening quotation
year = 2016
f'Results of the {year}'

# 2. str.format() method 
# You’ll still use { and } to mark where a variable will be substituted
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)

# 3. Finally, you can do all the string handling yourself by using string slicing and concatenation operations to create any layout you can imagine
s = 'Hello, world.'
str(s) # values which are fairly human-readable,

repr(s)# meant to generate representations which can be read by the interpreter

# Formatting String Literals
# let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
print(f'My hovercraft is full of {math.pi:.3f!s}.') #  convert the value before it is formatted '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():

# Positional and keyword arguments can be arbitrarily combined:
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# File manipulation
f = open('workfile', 'w', encoding='utf-8') # open file in write mode
f.write('Hello World') #write to file
f = open("workfile", "r") # read mode
print(f.read()) # actual read
with open('workfile', encoding="utf-8") as f:
    read_data = f.read() # read from file
    print(read_data)
f.readline() reads a single line from the file
f.close()

# Saving structured data with JSON
import json
x = [1, 'simple', 'list']
json.dumps(x)
""")