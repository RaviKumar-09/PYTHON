s = "hll wrld"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print(count) 