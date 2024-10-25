from collections import Counter
my_list = [1, 2, 2, 3, 3]
most_common = Counter(my_list).most_common(1)[0][0]
print(most_common)