"""
Hello there
My name is Maira Iantas and this is my first time using python
I will start this documentation today and I will check in the future the 
the progress that I've made, let's check it out

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
Copied from  :https://www.w3schools.com/python/python_datatypes.asp
"""
# Settings the DataTypes / Specific DataTypes

#string
example = "Hello World"          # or str("Hello World")
print(type(example))

#int
example = 20                     # or int(20)
print(type(example))

#float/decimal
example = 20.5                   # or float(20.5)
print(type(example))

#complex
example = 1j                     # or complex(1j)
print(type(example))

#list                  
example = ["a","random","list"]  # or list(("a", "random", "list"))
print(type(example))

#tuple
example = ("a","simple","tuple") # or tuple(("a", "simple", "tuple"))
print(type(example))

#range
example = range(6)              # n/a
print(example)
print(type(example))

#dict
example = {"firstName" : "Lady", "lastName" : "Gaga"} # or dict(firtName="Lady", lastName="Gaga")
print(type(example))

#set
example = {"a","simple","set"}   # or set(("a", "simple", "set"))
print(type(example))

#frozenset
example = {"a","simple","frozenset"}  # or frozenset(("a", "simple", "frozenset"))
print(type(example))

#boolean
example = True
print(type(example))                  # or bool(1) 

#bytes
example = b"Hello"                    # or bytes(5)
print(type(example))

#bytearray
example = bytearray(5)                # or bytearray(5)
print(type(example))

#memoryview
example = memoryview(bytes(5))        # or memoryview(bytes(5))
print(type(example))
