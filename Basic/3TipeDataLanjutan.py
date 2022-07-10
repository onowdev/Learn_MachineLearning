"""Python Data Types
Built-in Data Types
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
# example

x = 5
print(type(x))

Namaku = "Andra"
print(type(Namaku))

a = 80.98
print(type(a))

b = 9j
print(type(b))

c = ["Appel", "Banana", "Cherry"]
print(type(c))

d = {"Appel", "Banana", "Cebong"}
print(type(d))

e = ("apple", "Banana", "Cherry")
print(type(e))

f = range(9)
print(type(f))

g = {"Name" : "Joni", "age": 30}
print(type(g))

h = frozenset({"Apple","Banana","cherry"})
print(type(h))

j = True
print(type(j))

k = b"Hello"
print(type(k))

l = bytearray(9)
print(type(l))

m = memoryview(bytes(9))
print(type(m))

n = None
print(type(n))

""" Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions: """

