print("""
# CLASSES
# Blueprint for creating instances
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

emp_1 = Employee('Jane', 'Doe',50000)
emp_2 = Employee('John', 'Doe', 120000)
print(emp_1.fullname())
# Instance of Class

# Instance Variables and Class Variables

# Instance Variables
set for data that is unique to each instance using the self urgument and are unique to each variable
# Data that is unique to each instance

# Class Variables
Variables shared among all instances of a class. Class variables are the same for all instances while instance variable are unique to each instance variable

class Employee:
    # CLASS VARIABLE
    num_of_empls = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_empls += 1

    def fullname(self):
        return '{}{}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # using instance variable if defined || 
        self.pay = int(self.pay * Employee.raise_amount) # using the class varible

    # Class method

# METHODS REGULAR Methods, CLASS Methods and STATIC Methods
# 1. Regular Methods
Take the instance(self) as the first urgument

# 2. Class Method
Take the class(cls) as the first urgument and are preceeded by @classmethod

# 3. Static Method
Do not pass any ARGUMENT(s)
use because they have a logical connection to the class

class Employee:
    # CLASS VARIABLE
    num_of_empls = 0
    raise_amount = 1.04
    #REGULAR METHOD
    def __init__(self, first, pay):
        self.first = first
        self.pay = pay
    #CLASS METHOD
    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def parse_string(cls, string):
        first, last, pay = string.split('/')
        return cls(first,last,pay)

    # STATIC METHOD
    @statimethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return false
        return True

# Class method in use
employee1 = 'jane/doe/10000'
employee2 = Employee.parse_string(employee1)
print(employee2)

Employee.set_raise_amount(1.05)
emp1 = Employee('jane', 10000)
emp2 = Employee('Mike', 20000)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)

#Static method in use
import datetime
mydate = datetime.date(2022,12,25)
print(mydate.weekday())
print(Employee.is_workday(mydate))

# INHERITANCE   
class Developer(Employee): #inherits from Employee class

class Employee:
    # CLASS VARIABLE
    num_of_empls = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_empls += 1

    def fullname(self):
        return '{}{}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # using instance variable if defined || 
        self.pay = int(self.pay * Employee.raise_amount) # using the class varible

class Developer(Employee):
    def __init__(self, first, last, pay, prg_lang):
        super().__init__(first, last, pay)
        self.prg_lang = prg_lang
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else: 
            self.employees = employees
    #Add
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    #Remove
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    #ShowAll Emps
    def all_emps(self):
        for emp in self.employees:
            print("--->",emp.fullname())
        
emp1 = Developer('Jane', 'Doe', 12000, 'Javaa')
emp2 = Developer('Kerry', 'Manej', 12040, 'Python')
man1 = Manager('Hellen', 'Osotsi', 90000, [emp1])
man1.add_emp(emp2)
man1.all_emps()
man1.remove_emp(emp2)
print("Before remove")
man1.all_emps()

print(isinstance(man1, Manager))
print(issubclass(Developer, Manager))

# SPECIAL/DUNDER METHODS
    def __repr__(self):
        return "Employee('{}', '{}','{}')".format(self.first, self.last, self.pay)
    def __str__(self):
        return "Employee('{} - {}')".format(self.fullname(), self.email)
    def __add__(self, other):
        return self.pay + other.pay

""")