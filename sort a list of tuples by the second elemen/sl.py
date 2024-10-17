my_list = [(), (3, ), (4)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)