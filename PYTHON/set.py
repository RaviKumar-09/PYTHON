s = set('s')
print(type(s))


s = set()
s.add(1)
s.add(90)
s.add(66)
print(s)

s = {1,2,3,4,4}
s.update('x','y','z')
print(s)

s = {1,2,3,4,4}
s.pop()
print(s)

s = {1,2,3,4,4}
s.remove(2)
print(s)


"""s = {1,2,3,4,4}
s.remove()
print(s)
"""

s = {1,2,3,4,4}
s.discard(2)
print(s)

print('clear')
s = {1,2,3,4,4}
s.clear()
print(s)


s = {1,2,3,4,4}
s.discard(2)
print(s)


print("UNION")
a = {2,3,6,7}
b = {2,3,6,7}
c = a.union(b)
print(c)

print("UNION")
a = {2,3,6,7}
b = {4,5,8,9}
c = a | b
print(c)

print("INTERSECTIONS")
a = {2,3,6,7}
b = {2,3,6,7}
c = a.intersection(b)
print(c)

print("INTERSECTION")
a = {2,3,6,7}
b = {2,3,6,7}
c = a & b
print(c)

print("DIFFRENCE")
a = {10,20,30,40}
b = {20,80,70,200}
c = a.difference(b)
print(c)


print("DIFFRENCE")
a = {10,20,30,40}
b = {20,80,70,200}
c = a - b
print(c)


print("SYMMENTRIC DIFFRENCE")
a = {10,20,30,40}
b = {20,80,70,200}
c = a.symmetric_difference(b)
print(c)


print("SYMMENTRIC DIFFRENCE")
a = {10,20,30,40}
b = {20,80,70,200}
c = a ^ b
print(c)


print("SYMMENTRIC DIFFRENCE")
a = {10,20,30,40}
b = {20,80,70,200}
c = b ^ a
print(c)