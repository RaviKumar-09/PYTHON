def find_second_largest(arr):
    if len(arr) < 2:
        return "Array must contain at least two elements."

    # Initialize first and second largest to minus infinity
    first_largest = second_largest = float('-inf')
    
    for num in arr:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest > num > second_largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else "No second largest found."