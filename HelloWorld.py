"""
Hello there
My name is Maira Iantas and this is my first time using python
I will start this documentation today and I will check in the future the 
the progress that I've made, let's check it out
"""

# This project was coded using VS Core
# Python 3.9.5

print("Hello World!")
print("Python --version to get the version #")

if 5 > 2 :
    print("Example 1: This is a simple if result where 5 > 2 is true")

# Declaring Variables:
# There is no command to declare variables

strVariable = "This is a string" #'This is also a string'
intVariable = 1
floatVariable = 2.0

print(strVariable)
print(intVariable)
print(floatVariable)
print("-------------------------")

# Casting 
 
thisWillBeString = str(100)
thisWillBeInt = int(100)
thisWillBeFloat = float(100)

print(type(thisWillBeString))
print(type(thisWillBeInt))
print(type(thisWillBeFloat))

print("-------------------------")

# Multiple Variables
firstName, SecondName, LastName = "Lady","Amazing","Gaga" # we can use '' as well
print(firstName)
print(SecondName)
print(LastName)
print("-------------------------")

favorite = color = ever = "Light Pink"
print(favorite)
print(color)
print(ever)
print("-------------------------")

# Unpack Collection
cities = ["airdrie", "calgary", "edmonton"]
x, y, z = cities
print(x)
print(y)
print(z)
print("-------------------------")

#Output variables
x = "python"
print("I am learning " + x)
print("-------------------------")

y = "I am learning "
z =  y + x
print(z)
print("-------------------------")


