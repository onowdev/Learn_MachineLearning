"""
Python - Global Variables
Variables that are created outside of a function 
(as in all of the examples above) are known as global variables.
Global variables can be used by everyone, 
both inside of functions and outside.
"""
# contoh
x = "Awesome"

def myFunc():
    print("Python is " + x)

myFunc()

print("Python is " + x)