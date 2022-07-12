"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""
print("Hello_World!")
#same AS
print('Hello_world!')

#Assign String to a Variable Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Makan_Pagi"
print(a) # mencetak Variabel a ke Layar

# Multiline Strings You can assign a multiline string to a variable by using three quotes:

b = """ 
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum.
"""

print(b)

"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""
c = "Hello_World"
print(c[2])

"""
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""

for x in "Banana":
    print(x)

"""
String Length
To get the length of a string, use the len() function.

"""
d = "Mouson Barat"
print(len(d))

"""
Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.
"""
txt = "Python adalah salah satu bahasa pemrograman yang bisa di terapkan pada Web sebagai backend dengan Django atau Flash sebagai Framework nya"
print("Web" in txt) # Output menghasilkan Boolean bernilai True