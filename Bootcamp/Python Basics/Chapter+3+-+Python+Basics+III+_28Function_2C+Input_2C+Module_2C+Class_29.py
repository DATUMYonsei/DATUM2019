
# coding: utf-8

# # Chapter 3 - Python Basics III

# So far, we have learned the data types used in python, assigning variables and ways to use conditional and loop statements.
# 
# In this chapter, we will discuss about functions, modules, class and how python work in "macro-level" approach

# ------------------------------

# ## Functions
# 
# 
# A function is a reusable block of code that you can call repeatedly to make calculations, output data, or really do anything that you want.
# 
# Simply speaking, you put something in, then you get something out.
# 
# This is one of the key aspects of using a programming language. To add to the built-in functions in Python, you can define your own!

# ![function.png](attachment:function.png)

# The input (or inputs) goes inside the bracket, while the output is stated mostly in the end of the definition of the function. 
# 
# Functions are defined with def, a function name, a list of parameters, and a colon. Everything indented below the colon will be included in the definition of the function.
# 
# __However, the function does not always require an input or output__

# ### Function with no input

# In[11]:

# Example 1

# No input

def hello_world():
    """ Prints Hello World!"""
    print("Hello World!")

hello_world()


# In[2]:

for i in range(5):
    hello_world()


# These type of functions are used in the following way:
# 
# _variable = function()_

# ### Function with no output

# In[15]:

# Example 2

# No output

def sum(a,b):
    print("the sum of {0} and {1} is {2}".format(a,b,a+b))
    
a = sum(3,4)


# In[20]:

print(a) # Output can only be shown with "return" inside the function


# These type of functions are used in the following way:
# 
# _function(input1, input2 ....)_

# ### Function with no input nor output

# In[18]:

def say():
    print("Hi")
    


# In[19]:

say()


# These type of functions are used in the following way:
# 
# __function()__

# ### Function in General

# #### as any variable defined purely within a function will not exist outside of it.

# In[3]:

def see_the_scope():
    in_function_string = "I'm stuck in here!"

see_the_scope()

print (in_function_string) # This will not work


# The scope of a variable is the part of a block of code where that variable is tied to a particular value. Functions in Python have an enclosed scope, making it so that variables defined within them can only be accessed directly within them. 
# 
# If we pass those values to a __return__ statement we can get them out of the function. This makes it so that the function call returns values so that you can store them in variables that have a greater scope.
# 
# In this case specifically,including a return statement allows us to keep the string value that we define in the function.

# In[21]:

def free_the_scope():
    in_function_string = "Anything you can do I can do better!"
    return in_function_string

my_string = free_the_scope()
print (my_string)


# In[22]:

# Example 2

def volume(length, width, depth):
    """ Calculates the volumne of a rectangular prism"""
    
    return length*width*depth

volume(4,7,5)


# ### Function with arbitrary inputs

# If we want to, we can define a function so that it takes an arbitrary number of parameters. We tell Python that we want this by using an asterisk (*).

# In[6]:

def sum_values(*args):
    sum_val = 0
    
    for i in args:
        sum_val += i
    
    return sum_val


# In[7]:

print(sum_values(1,2,3,4,5))
print(sum_values(1,2,5))


# The time to use *args as a parameter for your function is when you do not know how many values may be passed to it, as in the case of our sum function. The asterisk in this case is the syntax that tells Python that you are going to pass an arbitrary number of parameters into your function. These parameters are stored in the form of a __tuple__.

# In[8]:

def test_args(*args):
    print (type(args))

test_args(1, 2, 3, 4, 5, 6)


# ### Function only has one return value

# In[28]:

def sum_and_mul(a,b):
    return a+b, a*b

def sum_and_mul_fake(a,b):
    return a+b
    return a*b


# In[29]:

result = sum_and_mul(2,5)
print(result) # The result is 1 tuple value

result2 = sum_and_mul_fake(2,5)
print(result2) # only returns 1 result


# ------------------------------

# ## User Input and Print

# ![input.png](attachment:input.png)

# Most of the programs and software that we use today, requires user input. Login, password are representative examples. In this part, we will learn how to adopt user input with python

# In[31]:

a = input() # enter what you want to say!


# In[32]:

a


# ### Receiving User input via prompt

# In[34]:

input("Please enter your favorite color")


# ### Printing results in a single line

# In[35]:

for i in range(0,10):
    print(i)


# In[37]:

for i in range(0,10):
    print(i, end=" ")


# In[44]:

for i in range(0,10):
    print(i, end="and")


# ### Printing Strings

# In[48]:

print("I" "love" "you" "so" "much")
print("I"+"love"+"you"+"so"+"much")

# Comma provides space
print("I " "love " "you " "so " "much ")
print("I","love","you","so","much")

# Enter (line change)
print("H""\n""i")

# Tab
print("this","is","\t","tab")


# ------------------------------

# ## Class

# ![class.jpg](attachment:class.jpg)

# This picture above explains the definition of class in the best way.
# Class is the stamp that shapes the cookies (objects/variables). They allow programmers to create variables with same characteristics defined by the class.  
# 

# __Functions__ : they __do__ specific things
# 
# __Classes__: they __are__ specific things
# 
# Let's look at the examples and see what exactly Class is

# In[72]:

# Example 0.5

class Calculator:
    pass

a = Calculator()
type(a)


# In[76]:

# Example 1

class Calculator:
    def data(self, first, second):
        self.first = first
        self.second = second
    
    def sum(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


a = Calculator()

a.data(2,5)

print(a.sum(), a.sub(), a.mul(), a.div())


# In[67]:

# Example 2

# Making a cookie stamp
class Employee:
    """Common basic information of all employees"""
    empNum = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empNum += 1
    
    def show_empNum(self):
        print ("Total Employee Number is {0}".format(Employee.empNum))
        
    def show_empInfo(self):
        print ("Name: ", self.name, ", Salary: ", self.salary)


# In[68]:

# Stamping cookies

emp1 = Employee("Jake","3000")
emp2 = Employee("Mina","2000")
emp3 = Employee("John","1000")
emp4 = Employee("Mike","500")


# In[70]:

# Using functions defined in class

emp1.show_empInfo()
emp2.show_empInfo()

print("\n")

emp3.show_empNum()
emp4.show_empNum()


# In[60]:

print("Total Employee Number = " + str(Employee.empNum))


# _________________

# ## Modules

# Module is a file that contains classes, variables or functions. It is a python file that can be "imported" and used. Python programmers can share modules and use them in their own code by importing the modules.

# In[78]:

from IPython.display import IFrame

# Importing Iframe function from Ipython  display file


# ![Screenshot%20from%202018-01-09%2002-14-42.png](attachment:Screenshot%20from%202018-01-09%2002-14-42.png)![Screenshot%20from%202018-01-09%2002-21-30.png](attachment:Screenshot%20from%202018-01-09%2002-21-30.png)

# In[91]:

IFrame("http://comic.naver.com", width=800, height=300)


# ### Installing Modules

# Every computer has a path, or directory. It works like an address.
# 
# "C:/Users/username/Desktop" --> this is probably your 바탕화면 address
# 
# python would also exist in a folder somewhere in your computer. If your path has been set properly, you can call pip to install required python modules.
# 
# In the command prompt, you can type
# 
# __pip3 install module_name__ or __python3 -m pip install module_name__
# 
# Depending on your environment variable, calling your pip can be slightly different.
# 

# ![pip.png](attachment:pip.png)

# In[ ]:



