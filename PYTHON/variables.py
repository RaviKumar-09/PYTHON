#Creating Variables
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

#String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

#Case-Sensitive
#Variable names are case-sensitive.
#This will create two variables:
a = 4
A = "Sally"
#A will not overwrite a

#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:

"""2myvar = "John"
my-var = "John"
my var = "John"""


#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "John"

#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "John"

#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:

#ExampleGet your own Python Server
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Note: Make sure the number of variables matches the number of values, or else you will get an error.

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
#Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python - Output Variables
#Output Variables
#The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)

#Global Variables
#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Local Variable
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

#ExampleGet your own Python Server
#A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc()

#Function Inside Function
#As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
#The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

