
# coding: utf-8

# # Chapter 2 - Python Basics II

# In the previous chapter, we learned about different data types. In comparison to learning English, we finished our alphabets. This chapter will cover how to use data types. It is time to learn about Pythonic grammar! 

# ------------------------------

# ## Variables

# We have already learned about assigning variables with different data types. In this section, more advanced approach of assigning variables will be shown 

# In[3]:

# You can assign variables like this
a,b = ("Python", "Grammar")

print(a)
print(b)

# Remember, that tuple can skip brackets!
c,d = "Maplestory", "Crazy Arcade"

print(c)
print(d)


# In[6]:

e = f = "python"
print(e)
print(f)


# In[7]:

[g,h] = ["Coding","is fun"]
print(g)
print(h)


# You can switch or reassign values like this

# In[9]:

a = 3
b = 5

# Switch!
a,b = b,a

print(a)
print(b)


# In[11]:

a = 4

# reassigning variable a
a = a+1
print(a)


# ------------------------------

# ## Control Statements
# 
# Control and Loop statements are the basic structure of coding. They are the algorithm and flow of the code execution. Codes are executed line by line, one at a time from top to bottom. The sequence of statements that are executed is referred to as the __flow of control__. The flow of control can be changed with the control statements: conditional and loop statements.
# 
# _conditional_
# - if
# 
# _loop_
# - while
# - for
# 
# When using these control statements, __Indentation__ and __:__ is very very very important. Conditional and Loop statements are frequently used together

# ### Conditional Statement - if
# 
# conditional statements are statements that may or may not be executed depending on certain conditions that the code specifies. The condition part is where __Boolean data types__ and __logical operators__ are used frequently

# Example)
# 
# Let's assume that there is a movie rated R, which means that the movie can only be watched by people restricted to the age 18 and over. We have to screen out people with appropriate ages. Your cousin is age 14. Let's try this out using if statement

# In[12]:

age = 14

if age < 18:
    print("You are not allowed to watch this movie")

else:
    print("Enjoy the movie!")
    


# #### Structure
# 
# We can create segments of code that only execute if a set of conditions is met. We use if-statements in conjunction with logical statements in order to create branches in our code.
# 
# An if block gets entered when the condition is considered to be True. If condition is evaluated as False, the if block will simply be skipped unless there is an else block to accompany it. Conditions are made using either logical operators or by using the truthiness of values in Python. An if-statement is defined with a colon and a block of indented text.

# ![if.png](attachment:if.png)

# In[17]:

# This is the basic format of an if statement. This is a vacuous example. 

if "Condition1": 
    # This block of code will execute because the string is non-empty
    # Everything on these indented lines
    print (True)
else:
    # So if the condition that we examined with if is in fact False
    # This block of code will execute INSTEAD of the first block of code
    # Everything on these indented lines
    print (False)


# In[18]:

# If you want more than two control line, you should use "elif"

if "Condition": 
    # Everything on these indented lines
    print (True)

elif "Condition2":
    # This block of code will execute only if the previous statement is false
    # Everything on these indented lines
    print("What?")
    
elif "Condition3":
    # Everything on these indented lines
    print("What??")
    
else:
    # This block of code will execute INSTEAD of the first and the second block of code
    # Everything on these indented lines
    print (False)
    


# __Ways to write condition statements__
# 
# |various expressions
# |:--
# | x < y , x > y 
# | x == y, x != y
# | x >= y, x <= y
# | x or y
# | x and y
# | not x 
# | x in list , x not in list
# | x in tuple , x not in tuple
# | x in string , x not in string

# In[19]:

# Example 1

money = 3000
feeling = "bad"

if money < 3000:
    print("Walk")

elif money >= 3000 and feeling == "good":
    print("Take Bus")
    
else:
    print("Take Taxi")


# In[30]:

# Example 2

menu = {"ramen":["flour","egg","pork","onion"],
       "spaghetti":["flour","cream","tomato","beef","onion"],
       "kimbap":["rice","carrot","spam","egg","spinach","pickle"]}

if "flour" not in menu["ramen"]:
    print("I will eat ramen!!!")

elif "kimbap" in menu.keys():
    print("Give me donkatsu")
    
else:
    print("spaghetti for me please")


# In[31]:

# Example 3

i = 10
if i % 2 == 0:
    print("{0} is even number!!!".format(i))
    
    if i % 3 == 0:
        print ('{0} is divisible by both 2 and 3! Wow!'.format(i))
    elif i % 5 == 0:
        print ('{0} is divisible by both 2 and 5! Wow!'.format(i))
    else:
        print ('{0} is divisible by 2, but not 3 or 5. Meh.'.format(i))
else:
    print ('{0} is an odd number.'.format(i))


#  

#  

# ### Loop Statement - For

# For is a loop statement used for going through values or iterate over any sequences (tuple, list, string). 

# In[35]:

# Example 1

for i in range(0,5):
    print (i) 


# In[36]:

# Example 2

for i in range(5):
    print (i) 


# In[37]:

# Example 3

a = [(1,2),(3,4),(5,6)]

for (x,y) in a:
    print(x+y)


# In[ ]:

# Example 4

result = []

for i in range(2,5):
    for j in range(3,6):
        result.append(i*j)

print(result)


# #### Stopping the Loop

# In[38]:

for i in range(5):
    if i == 2:
        break
    print (i)


#  

#  

# ### Loop Statement - While

# with While loops we need to make sure that something actually changes from iteration to iteration so that that the loop actually terminates.
# 
# If not, the infinite loop will be created, and your code execution will not stop. In this case, we use the shorthand i -= 1 (short for i = i - 1) so that the value of i gets smaller with each iteration. Eventually i will be reduced to 0, rendering the condition False and exiting the loop. Or, you can use __break__ or use __conditional statements__ to stop the loop

# In[45]:

# Example 1

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("Tree hit %d times." % treeHit)
    if treeHit == 10:
        print("Tree falls.")


# In[46]:

# Example 2

i = 10
while True:
    if i == 14:
        break
    i += 1 # This is shorthand for i = i + 1.
    print( i)


# In[52]:

# Example 3

Stamina = 50
apple = 3

while Stamina>0:
    Stamina -= 5
         
    while Stamina < 10 & apple > 0:
        print("Eat apple")
        Stamina += 10
        apple -= 1
        print("Remaning apple is {0}".format(apple))
   
    print("Current Stamina is {0}".format(Stamina))
    
    if Stamina == 0:
        print("You are Dead")
    else:
        pass 


# ### Break, Continue, Pass
# 
# __Break, Continue, Pass__ statements are used to work with loop and conditions more efficiently and effectively.
# 
# __Break__ statements provide the opportunity to stop and exit the loop completely when external condition is triggered. 

# In[54]:

number = 0

for number in range(10):
    number = number + 1

    if number == 5: # external condition
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')


# __Continue__ statements allows you to skip over a part of loop when external condition is triggered, but go on to complete the rest of the loop. 

# In[55]:

number = 0

for number in range(10):
    number = number + 1

    if number == 5: # external condition
        continue    # break here

    print('Number is ' + str(number))  # Number is 5 will not be printed

print('Out of loop')  


# __Pass__ statement allows to handle the condition without the loop being impacted in any way. |

# In[56]:

number = 0

for number in range(10):
    number = number + 1

    if number == 5: # external condition
        pass   # break here

    print('Number is ' + str(number)) 

print('Out of loop')  


# ------------------------------
