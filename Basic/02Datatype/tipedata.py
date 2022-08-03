""" py type data"""
"""Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories: 

Text Type       :	str
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview
None Type       :	NoneType
"""
# str type
a = "python is awesome"
print(type(a))
# Num Type
b = 90
c = 8.9
d = 9j
print(type(b))
print(type(c))
print(type(d))
# Squence types
e = ["apple", "banana", "Cherry"]
f = ("apple", "Banana", "Cherry")
g = range(9)
print(type(e))
print(type(f))
print(g)
print(type(g))
# Mapping Type
h = {"Name":"andra", "Age":6}
print(h)
print(type(h))

# Set Type
i = {"apple", "banana", "cherry"}
j = frozenset({"apple","banana","cherry"})
print(i)
print(type(i))
print(j)
print(type(j))

#boolean type
k = True
l = False
print(k)
print(type(k))
print(l)
print(type(l))

#binary Type
m =b"hello"
n = bytearray(9)
o = memoryview(bytes(9))

print(m)
print(type(m))
print(n)
print(type(n))
print(o)
print(type(o))

# None Type
p = None
print(p)
print(type(p))