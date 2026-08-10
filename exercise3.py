# Quick Start with Python
## Note1: Comments after pound(#) won't be executed
## Note2: To run one line, place your mouse there,  right-click and choose "Execute Line in Python Console"
## Note2: To run multiple lines, select them and right-click to choose "Execute Selection in Python Console"


# 1. Python Basics
## 1.1 Strings
sentence = "Hello Everyone"               # Either double quote or single quote are fine
print(sentence)                           # print the variable

len(sentence)     # Strings are indexable, check the length first
sentence[5]       # Select character in the 6th position: python index starts from 0
sentence[:5]      # Select the first 5 characters: index 0,1,2,3,4 only, same as sentence[0:5]
sentence[5:]      # Select all characters starting from the 6th (index 5)

#sentence[0] = 'H'                        # Strings are not mutable, ERROR here if executed
'Morning' + sentence[5:]                  # Replace first 5 characters by concatenating two strings

## 1.2 Lists
lst = [1, 2, 3, 4, 5]           # Create a list variable lst1
1 in lst                        # Membership operators: in, not in
lst[4]                          # Lists can be indexed
lst[4] = 6                      # Lists are mutable


# 2. Flow Control
## 2.1 The for-loop (Execute Selection)
for i in lst:
    print(i * 10 + 1)                  # Indentation (press the tab key)

## 2.2 Combine for-loop with if-else statement (Execute Selection)
for i in lst:
    if i <= 2:                         # 1st indentation
        print(i, "is in the bottom.")  # 2nd indentation
    elif (i > 2) and (i <= 4):
        print(i, 'is in the middle.')
    else:
        print(i, "is in the top.")


# 3. Python functions and Modular Programming
## 3.1 Built-in functions
round(13.136784, 2)    # Round a number to certain decimal places

## 3.2 Define a custom function (Execute Selection)
def greet(name):
    print("Hello, " + name + ". How are you today?")

def compare(a, b):
    if a < b:
        print(str(a) + " is smaller than " + str(b) + ".")
    elif a > b:
        print(str(a) + " is greater than " + str(b) + ".")
    else:
        print(str(a) + " is equal to " + str(b) + ".")

## 3.3 Apply the two functions by specifying parameter values
greet(name = 'Alice')         # Same as gree('Alice')
compare(a = 2.0, b = 2)       # Same as compare(2.0,2)


##  3.3 Modular Programming
## Step 1: save the above codes in 3.2 in a new python script and name the file as my_module.py
## Step 2: import the file, run those functions by assigning new param values
import my_module
help(my_module)              # Check the module out

my_module.greet('Richard')   # Use functions after the module name with the .method
my_module.compare(1, 2)

from my_module import greet  # Alternatively, import a function from a module directly
greet('Alice')