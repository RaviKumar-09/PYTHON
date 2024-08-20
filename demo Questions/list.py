# Lists

mylist = [1,2,3,4,5]
#mylist  = ['hbdhgiud,1,1,2,True,[1,2,3,4]']
print(len(mylist))
print(mylist[1])
print(mylist[1:4])

mylist = ['a','b','c']
print('before reassignment')
print(mylist)

mylist[0] = "RAVI"
print('after reassignment')
print(mylist)

#index
print("index")
mylist = [1,2,3,4,5]
print(mylist[1])

#sliceing
print('sliceing')
mylist = [1,2,3,4,5]
print(mylist[:3])

#append

mylist = [1,2,3,4,5]
mylist.append("RAVI")
print(mylist)

#insert

print('insert')
n  = [1,2,3,4,5,6]
x = n.insert(333,4,)
print(x)


#extend
print("extend")

order1 = ["chicken","mutton","fish"]
order2 = ["biriyani"]
order1.extend(order2)
print(order1)

#pop
mylist = ['a' , 'b' , 'c' , 'd' , 'e']
item = mylist.pop()
print(item)
item = mylist.pop(2)
print(item)

#reverse

mylist = ['a' , 'b' , 'c' , 'd' , 'e']
mylist.reverse()
print(mylist)


#sort
print("sort")
mylist = ['a' , 'b' , 'e' , 'd' , 'c']
mylist.sort()
print(mylist)


#nestedlisIndex
print("nestedlisIndex")
mylist = [1,2,['x','y','z']]
print(mylist[2][1])


#list_comprehesions
print('list_comprehesions')
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ravi = matrix[0][0]
print(matrix)
print(ravi)

dhoni = [row[0] for row in matrix]

print(dhoni)