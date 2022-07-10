"""
Python Numbers
There are three numeric types in Python:

1. int >> Int or integer, is a whole number, 
positive or negative, without decimals, 
of unlimited length.

2. float >> Float or "floating point number" 
is a number, positive or negative, containing 
one or more decimals.

3. complex >> Complex
Complex numbers are written 
with a "j" as the imaginary part:


Random Number
Python does not have a random() 
function to make a random number, 
but Python has a built-in module 
called random that can be used to 
make random numbers:
"""
import random

x = 1
y = 9.9
z = 9j

print(type(x))
print(type(y))
print(type(z))

print(random.randrange(1,20))