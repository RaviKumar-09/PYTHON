s = "11112233"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print(count) 