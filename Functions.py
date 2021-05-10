"""
Hello there
My name is Maira Iantas and this is my first time using python
I will start this documentation today and I will check in the future the 
the progress that I've made, let's check it out
"""
# Functions
x = "Python"

def myfunc():
    print("I am learning " + x)

myfunc()

print("-------------------------")
def mySecondFunc():
    global x
    x = "fantastic"

mySecondFunc()

print("Python is " + x)
print("-------------------------")