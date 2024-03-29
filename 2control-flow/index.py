print("""
# CONTROL FLOW
# IF statement
x=2
if x<0:
    print("X is -ve no")
elif x>1:
    print("X is +ve no)
else: 
    print("No num entered")

# FOR loop (can iterate through items in a sequence list/string)
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w)) 

# Using RANGE 
nums=["one", "two", "three", "four", "five", "six"]
for num in range(0, len(nums)):
    print(nums[num]) 

# Using ENUMERATE prints both index and value used with keyword ""list""
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

# Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# BREAK and CONTINUE Statements
a loop\’s ELSE clause runs when no break occurs
breaks out of the innermost enclosing for or while loop
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')

continue
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# PASS statement does nothing, required syntactically but the program requires no action
def initlog(*args):
    pass   # Remember to implement this!

# MATCH statement only first pattern that matches gets executed/ similar to SWITCH
def http_error(status):
    match status:
        case 400 || 404: (combine several literals)
            return "Bad request"
        case _:
            return "Something's wrong with the internet"

# FUNCTIONS
def sayHello(name):
    # this is a DOCSTRINGS (documentation) of the function
    '''First line of DOCSTRINGS short func Description
      
    Other lines follow
    '''
    it\’s good practice to include docstrings in code that you write,
    print('Hello', name)

# all variable assignments in a function store the value in the local symbol table; 
whereas variable references first look in the local symbol table, then in the local 
symbol tables of enclosing functions, then in the global symbol table, and finally in 
the table of built-in names
# optional vs mandatory arguments
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    # keyword arguments && positional arguments
    print(prompt="only the first is a mandatory argument, rest are optional becoause there are defaults")
    # IN KEYWORD  in keyword tests whether or not a sequence contains a certain value
    if ok in ('y', 'ye', 'yes'):
        print("Conforms", ok)

# ARGUMENTS/PARAMETERS
# By default, arguments may be passed to a Python function either by POSITIONAL or explicitly by KEYWORD/NAMED parameters
# *name receives a tuple containing the POSITIONAL arguments can receive as many as possible
# **name is present, it receives a dictionary containing all KEYWORD/NAMED arguments can receive as many as possible
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?") 
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw]) 

cheeseshop("Limburger", "Hello", "World",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
# marking POSITIONAL(*) args and KEYWORD/NAMED(/) args
def combined_example(pos_only, /, standard, *, kwd_only):

# LAMBDA expression/key word
# to create Small anonymous functions  
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)// passes arg of parent function
f(3) // passes arg of lambda function

# FUNCTION ANNOTATIONS
# metadata information about the types used by user-defined functions
 # annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation
 # def f(ham: str, eggs: str = 'eggs') -> str

# NAMING CONVENTION CLASSES and FUNCTIONS
# the convention is to use UpperCamelCase for classes (SumCalculator)
# lowercase_with_underscores for functions and methods (sum_calculator)
""")