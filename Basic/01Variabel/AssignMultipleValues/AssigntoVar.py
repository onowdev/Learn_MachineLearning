"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x,y,z = "Orange", "Bananas", "Apple"
print(x)
print(y)
print(z)

#One Value to Multiple Variables And you can assign the same value to multiple variables in one line:

x = y = z = "Pinapple"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables.
# This is called unpacking.

fruits = ["Apple", "Banana", "Cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
