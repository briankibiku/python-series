print("""
# ARITHMETICS OPERATIONS EXPLAINED
# Single line comment denoted by a HASH sign (#)
# Multiline line comments denoted by a THREE QUOTES at Start and End \"""
# use \' to escape the single quote...
# Addition
2 + 2
# Divide (retruns a float)
4 / 2
# Floor Division (returns an int)
4 // 2
# Remainder of division
4 % 2
# Squaring a number 
2 ** 2
# Assignment operator = used to assign value to variable
weight = 5
# In interactive mode, the last printed expression is assigned to the variable _
2 + 2
_ 
prints 4

# STRINGS
# String concatination
 'un' + 'ium'
# Letter position in word
word = 'Python'
word[0] -> P
# Range at position 2 is excluded
word[0:2]

# LISTS 
# Mutable,comma seperated usually same data type values
squares = [1, 4, 9, 16, 25]

# slicing returns a new list
squares[-3:]  
[9, 16, 25]

# Array concatination 
squares + [36, 49, 64, 81, 100]

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list


#Adding items
squares.append(216)
# clear the list by replacing all the elements with an empty list [:] (used to indicate whole list)
squares[:] = []

# BOOLEAN
True and False

# Multiple Assignments
a, b = 0, 1
""")