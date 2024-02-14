for i in range(1,6):
    if i <= 3:
        print(i)


for i in range(1,6):
    if i <= 3:
        break
        print(i)
print('break')


for i in range(1,6):
    if i == 3:
        continue
    print(i)
print('continue')


for i in range(1,6):
    if i == 3:
        pass
    print(i)
print('pass')

for i in range(1,6):
    if i == 3:
        pass
    else:
        print(i)


i = [1,2,3,4,5,6,7,8,9]

for i in i:
    if i % 5 == 0 :
        print(i)
        break
else:   
    print("not found")