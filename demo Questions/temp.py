
"""def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")"""



"""# Input array
arr = [5, 2, 9, 1, 5]

# Sort the array in descending order
sorted_arr = sorted(arr, reverse=True)

# Print the sorted array
print("Sorted Array in Descending Order:", sorted_arr)"""


"""# Input array
arr = [5, 2, 9, 1, 5]

# Find the number of elements in the array
num_elements = len(arr)

# Print the number of elements
print("Number of elements in the array:", num_elements)"""


""""def left_rotate(arr, n, k):
    # left rotate the array by k
    for i in range(k):
        left_rotate_by_one(arr, n)

def left_rotate_by_one(arr, n):
    
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

# test the function
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 2
left_rotate(arr, n, k)
print("Left rotated array is: ", arr)"""


def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(10)) 
print(check_number(-10))
print(check_number(0)) 