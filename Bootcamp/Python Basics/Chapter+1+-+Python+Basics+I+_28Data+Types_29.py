
# coding: utf-8

# # Chapter 1 - Python Basics I

# ## Python is an intuitive language

# Python is very intuitive, compared to other programming languages. This is why people say that it is easy to learn for beginners. 
# 
# Let's look at the example below

# In[1]:

x = 3
if x ==3: print("correct")


# Just by reading this code, most people can catch what this code is saying.
# 
# The first line says that "x" equals to 3
# The second line says that if "x" equals to 3, print the word "correct"
# 
# Pretty easy eh?
#
# ------------------------------

# ## Code Comments

# Code comment is used for explanation from developers. They are ignored during code execution. Code comments can be made after a hashtag. For more multiple code comments, use of three quotations are used. Below is an example

# In[2]:

# This is a comment
# The comment section is ignored during the code execution


# The multiline comments do not perform anythin,

# In[12]:

"""
This is a multi-line comment. It is a special type of string called, Doc-string.
Normally, they are used for detailed explanation of codes, or long comments
"""


# ------------------------------

# ## Data Types
# 
# When you learn English, alphabet is the fundamental unit of knowledge. Python is also a programming __"language"__. Importance of data types are equivalent to knowing the alphabets.
# 
# These are main data types of python:
# 
# - Numbers
# - Strings
# - Boolean
# - Lists
# - Tuples
# - Dictionary
# - Set
# 
# Let's cover these data types one by one

# ### _Numbers_
# 
# Numbers include integers, floating numbers and complex numbers. If you have done your mathematics, these terms should be familiar. Also, there are octal and hexadecimal numbers which are not frequently used in general python programming. 
# 
# - integers --> _int_
# - floating number --> _float_
# - complex number --> _complex_
# 
# Let's look at them one by one

# #### Integer

# In[14]:

# Integer
## Integer is a real number. 
#It is a round number with no values after decimal point

x = 50

print(x) # Simple line that orders to show (print) x
type(x)  # This shows what the data type of x is


# Variables are assigned by using a single equation sign "=". They are case sensitive, but using similar variables are not recommended in a complex coding, due to confusion and readability

# In[15]:

one = 3
One = 6

print(one, One)


# #### Float

# In[20]:

# Floating Point
# Floating point is a name for a real number.
# It may have numbers after the decimal point

y = 1.4
z = 4.0

print(y)
print(z)

# you can use int() function to make float to integer
print(int(y))
print(int(z))

#You can use float() function to force a number to be considered as a float
my_int = 3
print(type(my_int))

my_int2 = float(3)
print(type(my_int2))


# #### Complex

# In[26]:

# Complex
# Complex is a complex number. 
# It is a number that can be expressed in the form of a + bi
# a, b are real numbers while i is the solution of x^2= -1

x = complex(2,4)
y = complex(1,5)

print(x,y, x + y)


# #### Basic Math

# Python has a number of built-in math functions. These can be extended even further by importing the math package or by including any number of other calculation-based packages.
# 
# All of the basic arithmetic operations are supported: +, -, /, and . You can create exponents by using * and modular arithmetic is introduced with the mod operator, %.

# In[28]:

print ('Addition: ', 2 + 2)
print ('Subtraction: ', 7 - 4)
print ('Multiplication: ', 2 * 5)
print ('Division: ', 10 / 2)
print ('Exponentiation: ', 3**2)
print ('Modulo: ', 15 % 4) # remainder


# This also works on variables

# In[29]:

first_integer = 4
second_integer = 5
print (first_integer * second_integer)

x = 3
x - 2


# In[30]:

first_integer = 11
second_integer = 3
print (first_integer / second_integer)


# __Python's built-in math functions__
# 
# - abs()
# - round()
# - max()
# - min()
# - sum()
# 
# These functions all act as you would expect, given their names. Calling abs() on a number will return its absolute value. The round() function will round a number to a specified number of the decimal points (the default is 00 ). Calling max() or min() on a collection of numbers will return, respectively, the maximum or minimum value in the collection. Calling sum() on a collection of numbers will add them all up. If you're not familiar with how collections of values in Python work, don't worry! We will cover collections in-depth in the next section.

# ### _Strings_

# string is a data type that lets you include text as a variable. They are defined using single quotes or double quotes
# 
# Both are allowed so that we can include apostrophes or quotation marks in a string if we so choose.
# 
# You may use \ to include apostrophes or quotation marks into the string

# In[33]:

say_hello = "Hello. My name is python"
print(say_hello)

say_bye = 'Bye. It was nice to meet you'
print(say_bye)

my_string = '"Jabberwocky", by Lewis Carroll'
print (my_string)

my_string = "'Twas brillig, and the slithy toves / Did gyre and gimble in the wabe;"
print (my_string)

alt_string = 'He said, \'this is ridiculous.\''
print(alt_string)


# #### Calculation in Strings

# In[36]:

# Addition
first_name = "Harry" 
last_name = "Potter"

first_name + last_name


# In[41]:

# Multiplication
twice = "likey"
twice*2


# In[42]:

# Usage
print("="*40)
print("Oh Yeah")
print("="*40)


# __Indexing and Slicing__

# In[51]:

sentence = "wingardium leviosa"

# Python starts from 0
print(sentence[4])
print(sentence[0])
print(sentence[-2])


# In[52]:

# Usage
print( sentence[11] + sentence[15] + sentence[13] + sentence[12])

# sentence[0:4] --> 0<= sentence < 4
print( sentence[0:4])


# In[56]:

# Changing string by indexing
a = "League of Leg nd"
print(a)

# You cannot change string or tuple. These are called imutable data types
a[-3] = "e"
print(a)


# In[63]:

correct = a[:7] + a[7:-3] + "e" + a[-2:]
print(correct)


# #### Formatting Strings

# Using the format() method we can add in variable values and generally format our strings.

# In[64]:

my_string = "{0} {1}".format('Marco', 'Polo')
print( my_string)

my_string = "{1} {0}".format('Marco', 'Polo')
print (my_string)


# We use braces ({}) to indicate parts of the string that will be filled in later and we use the arguments of the format() function to provide the values to substitute. The numbers within the braces indicate the index of the value in the format() arguments

# In[65]:

print ('insert %s here' % 'value')


# The % symbol basically cues Python to create a placeholder. Whatever character follows the % (in the string) indicates what sort of type the value put into the placeholder will have. This character is called a conversion type. Once the string has been closed, we need another % that will be followed by the values to insert. In the case of one value, you can just put it there. If you are inserting more than one value, they must be enclosed in a tuple.

# In[66]:

print ('There are %s cats in my %s' % (13, 'apartment'))


# #### Functions related to strings
# 
# - count()
# - find()
# - index()
# - join()
# - upper() / lower()
# - lstrip() / rstrip()
# - replace()
# - split()

# In[70]:

# Returns the number of character in the string
a = "Python is fun"

a.count("n")


# In[73]:

# Returns the value of first position. If does not exist, return -1
print(a.find("n"))
print(a.find("k"))


# In[74]:

# Returns the index number
print(a.index("s"))


# In[85]:

# Insert string a between 1 and 2
print(a.join("12"))


# In[86]:

# Change the characters to uppercase or lowercase
print(a.upper(), a.lower())


# In[89]:

# Deleting spaces in the left of right side of the string
b = "       I  have lots of      space   "
print(b.lstrip())
print(b.rstrip())

# Deleting spaces in both side of string
print(b.strip())


# In[90]:

# Replace
a.replace("fun","horrible")


# In[94]:

# Slicing
print(a.split())

# Another example
k = "I/do/not/like/your/shirt"
print(k.split("/"))
print(k.split("t"))


# #### Encoding

# Normal strings in python are stored internally as 8-bit (= 1byte) ASCII. On the other hand, unicode uses 16-bit system (= 2byte) and it can store a more varied set of characters.
# 
# Chinese characters and Korean characters cannot be represented in ASCII code.
# 
# ![encoding1.gif](attachment:encoding1.gif)

# UTF-8 strings are stored as 8 bit (= 1byte) just like ASCII, but it works as an extension of ASCII. It can express Korean also.

# ![encoding%20error.PNG](attachment:encoding%20error.PNG)

# Frequent errors that you can encounter

# In[217]:

a = "안녕"
b = a.encode("utf-8")
print(b)

c = b.decode("utf-8")
print(a)


# __str -- encode () --> bytes -- decode() --> str__

# ### _Boolean_

# Boolean is related to logical operators, and takes one of two values only: True or False (True = 1, False = 0)
# 
# Default Boolean values follows:
# 
# |Values|True of False|
# |:---|:----|
# |"python"| True|
# |""|False|
# |[]|False|
# |{}|False|
# |()|False|
# |0|False|
# |1|True|
# |[1,2,3]|True|
# |None|False|
# 
# Mostly, empty list,tuple,dictionaries are False. If not, they are True. In terms of numbers, 0 is False while 1 is true. 

# In[178]:

print(0 == 5)


# #### and (&) , or ( | ), not

# In[201]:

# And
print(True & True) # True and True
print(True & False) # True and False
print(False & False) # False and False

print("="*30)

# Or
print(True | True) # True or True
print(True | False) # True or False
print(False | False) # False or False

print("="*30)

# Not
print(not True)
print(not False)


# ### _Lists_

# List is an __ordered__ collection of objects that can contain any data type. List can be defined using brackets [ ]  

# In[97]:

eiffel_tower = ["Paris","France","1889",300.65, 324]


# We can access and index the list by using brackets as well. In order to select an individual element, simply type the list name followed by the index of the item you are looking for in braces.

# In[98]:

eiffel_tower[3]


# Indexing in Python starts from 00 . If you have a list of length nn , the first element of the list is at index 00 , the second element is at index 11 , and so on and so forth. The final element of the list will be at index n−1n−1 . Be careful! Trying to access a non-existent index will cause an error.
# 
# We can see the number of elements in a list by calling the len() function

# In[100]:

print(len(eiffel_tower))


# we can update and change list by accessing an index. List is mutable unlike strings meaning you can change them. However, once a string or other immutable data type has been created, it cannot be directly modified without creating an entirely new object.

# In[102]:

print(eiffel_tower[4])

eiffel_tower[4] = 320
print(eiffel_tower[4])


# If you want to put two lists together, they can be combined with a + symbol.

# In[103]:

# You can put list in a list!
list1 = ["i", 3, 4.30, [1,2,"harry"], "you"]
list2 = ["hello",4.5, 3.0]

list3 = list1 + list2
print(list3)


# __Indexing and Slicing__

# Lists have similar mechanism of indexing and slicing just as strings do

# In[107]:

starwars = ["may","the","Force","be","with","you"]

print(starwars[2:4])
print(starwars[1:])
print(starwars[:3])


# You can also add a third component to slicing. Instead of simply indicating the first and final parts of your slice, you can specify the step size that you want to take. So instead of taking every single element, you can take every other element.

# In[112]:

confusing = ["may",1,"the",2,"Force",3,"be",4,"with",5,"you"]
print(confusing[0:10:2])

print(confusing[::2])
print(confusing[::-1])
print(confusing[::-2])


# __Functions related with lists__
# 
# - append
# - sort
# - reverse
# - index
# - insert
# - remove
# - pop
# - count
# - extend

# In[114]:

# append
a = [1,2,3]
a.append(4)
a


# In[121]:

# sort
a = [2,5,3,4,7,1,3]
a.sort()
print(a)

b = ["c","d","b","w","f","r"]
b.sort()
print(b)


# In[122]:

c = [6,4,8,"e",3,"b","c"]

# This does not work
c.sort()


# In[123]:

a = ["a","c","b"]
a.reverse()
a


# In[125]:

a = [1,5,3,7]
a.insert(3,6)
a


# In[126]:

a = [1,2,3,4,5,6,7]
a.remove(5)
a


# In[127]:

a = [1,4,6]
a.pop()
a


# In[128]:

a = [1,4,7,3,5,6,"d"]
a.count("d")


# In[129]:

a = [1,2,3,4,5]
a.extend(["d","5","d",5])
a


# ### _Tuple_

# Tuple is similar to list.
# The difference between tuple and list is that tuple is immutable.
# The data cannot be changed once it has been generated.

# In[135]:

t1 = ()

# When tuple only has one value, comma must be follwed
t2 = (1,)
t3 = (1)

print(type(t2), type(t3))

# When assigning variable with tuple, brackets can be skipped 
t4 = (1,2,3)
t5 = 1,2,3

print(type(t4), type(t5))


# Tuple indexing and slicing is similar to list

# In[141]:

tup = (1,4,7,4,"d","d2",2,"4")

print(tup[4])
print(tup[2:])


# Tuple addition and multiplication

# In[138]:

tuple1 = (1,2,5)
tuple2 = (4,6,7)

tuple3 = tuple1 + tuple2
print(tuple3)

print(tuple2*4)


# ### _Dictionary_ 

# Dictionary is an important data structure in python. Dictionaries are defined with a combination of curly braces {} and colons : The braces define the beginning and end of a dictionary and the colons indicate key-value pairs. A dictionary is essentially a set of key-value pairs. The key of any entry must be an immutable data type. This makes both strings and tuples candidates. Keys can be both added and deleted.
# 
# In the following example, we have a dictionary composed of key-value pairs where the key is a genre of fiction (string) and the value is a list of books (list) within that genre. Since a collection is still considered a single entity, we can use one to collect multiple variables or values into one key-value pair.

# Dictionary Example
# 
# | Key | Value |
# |:----| :---- |
# | name| Jake  |
# |phone|01055999411|
# |birth|19941125|

# In[150]:

Personal_Info = {"name":"Jake",
                 "phone":"01055999411",
                "birth":"19941125"}


# #### Dictionary Usage & Manipulation

# In[142]:

Idols = {"Twice": ["Jihyo","Nayeon","Jungyeon","Momo","Sana","Mina","Dahyun","Chaeyoung","Tzuyu"], 
           "Blackpink": ["Jisu","Jennie","Rose","Lisa"],
           "Bigbang": ["GD","TOP","Taeyang","Daesung","Seungri"],
           "BTS": ["RM","Suga","Jin","J-Hope","Jimin","V","Jungkook"]}


# After defining a dictionary, we can access any values by indicating its key in brackets

# In[154]:

# Using Key to retrieve values

print(Idols["BTS"])
print(Idols["Twice"])


# Dictionary can be changed by the value associated with a given key

# In[145]:

Idols["Bigbang"] = ["GD","Top","Daesung","Taeyang"]
print(Idols["Bigbang"])


# #### Cautions when making dictionary
# 
# Dictionary Key is a unique value.
# This means that same key cannot be used again.
# Also, list cannot be used in the key. This will cause error

# In[161]:

# key cannot be used again (there are two "5"s in the key)
xdict = {5:"a", 5:"b"}

xdict # only returns 5:"b"


# #### Dictionary related functions
# 
# - keys
# - values
# - items
# - clear
# - get
# - in

# In[162]:

# Retrieve only "keys" from the dictionary
Idols.keys()


# In[163]:

# Retrieve only "values" from the dictionary
Idols.values()


# In[164]:

# Retrieve "keys" and "values" pairs from the dictionary
Idols.items()


# In[165]:

# Delete everything in the dictionary
Personal_Info.clear()
Personal_Info


# In[168]:

# Getting values with key
Idols.get("Blackpink")


# In[169]:

# Checking if key is in dictionary
"BtoB" in Idols


# In[170]:

"Bigbang" in Idols


# ### _Set_
# 
# Set is made with set() function. Set does not allow repetitive values, and it is unordered.

# In[180]:

s1 = set([1,2,3])
s2 = set("This is set")

print(s1, s2)


# Because set does not have orders, it cannot be indexed nor sliced.
# In order to perform this, they have to be converted to tuples or lists.

# In[182]:

l2 = list(s2)
print(l2)

print(l2[4])


# Set is useful when calculating intersection and union

# In[187]:

a = set([1,2,5,7,8,9])
b = set([2,6,3,8,4])

# Intersection
print(a & b)
print(a.intersection(b))

# union
print( a | b)
print(a.union(b))

# subtraction
print( a - b)
print( a.difference(b))


# __Set related functions__
# 
# - add
# - update
# - remove

# In[189]:

# Adding a value
s1 = set([1,4,6,7])
s1.add(9)

print(s1)


# In[191]:

# Adding multiple values
s2 = set([5,8,3])
s2.update([1,4,5,6])

print(s2)


# In[192]:

# Removing a value
s3 = set([2,5,8,1])
s3.remove(2)

print(s3)

