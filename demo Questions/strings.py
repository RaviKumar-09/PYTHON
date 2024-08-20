#STRINGS

'hello'
"hello"

"I'm a dog "

#Indexing

'''mystring = 'abcdefg'
print(mystring[-1])'''

#Slicing
'''mystring = 'abcdefg'
print(mystring[: : 1])'''

#basic methods

mystring = 'abcdefg'
x = mystring.upper()
print(x)


mystring = 'hello world'
x = mystring.split('o')
print(x)

mystring = 'hello world'
x = mystring.capitalize()
print(x)

#Print Formatting
x = "Insert another string here :{}" . format("INSERT ME!")
print(x)

x = "Insert one : {} Item two :{}" . format("dog","cat")
print(x)

x = "Insert one : {x} Item two :{y}" . format(y = "dog",x = "cat")
print(x)