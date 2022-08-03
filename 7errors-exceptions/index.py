print("""
# ERRORS AND EXCEPTIONS
# There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.


# Syntax Error
# Parse time errors
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
# The error is caused by (or at least detected at) the token preceding the arrow

# Exceptions
# Errors detected during execution
4 + spam*3
NameError: name 'spam' is not defined

# Handling Exceptions
while True:
    try:
        x = int(input('Enter a number'))
        break
    except ValueError:
        print('Opps, wrong data type')
#A try statement may have more than one except clause,
# An except clause may name multiple exceptions as a parenthesized tuple, for example:
  except (RuntimeError, TypeError, NameError):

# Defining Clean-up Actions
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


KeyboardInterrupt

""")