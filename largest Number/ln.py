#how to print the largest number in array

# using max () funtion

arr = [1,2,4,6,89]
largest = max(arr)

print(largest)


# using loops

arr = [1,34,55,668,2,1]
largest = arr[0]

for i in arr:
    if i > largest:
        largest = i
print(largest)