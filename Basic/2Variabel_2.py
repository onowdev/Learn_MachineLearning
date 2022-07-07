"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

"""
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
"""
a = b = c = "Apple"
print(a)
print(b)
print(c)

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. 
Python allows you to extract the values into variables. This is called unpacking.
"""
Buah = ["Apple", "Banana", "Water Melon", "Lechee", "Durian"]
e,f,g,h,i = Buah

print(e)
print(f)
print(g)
print(h)
print(i)