person = {"name": "Ravikumar", "age": 25, "city": "Palacole"}


for key in person:
    print(key)

for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
