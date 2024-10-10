list_of_lists = [[1, 2], [3, 4], [5, 6],[44.5,556],(667,900),[898,0000]]

kist = [item for sublist in list_of_lists for item in sublist]
print(kist) 