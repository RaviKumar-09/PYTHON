# Writing to a file
with open("test.txt", "r") as file:
    file.write("Hello, World!")

# Reading from a file
with open("test.txt", "w") as file:
    content = file.read()
    print(content) 
