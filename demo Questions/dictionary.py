d = {'key 1':'value 1','key 2':'value 2', 'key 3':'value 3', 'key 4':'value 4', 'key 5':'value 5' }
print(d['key 1'])


#nested Dic

d = {'key 1':'123','key 2':'value 2', 'key 3':'value 3', 'key 4':'value 4', 'key 5':{'123':[1,2,3]}}
print(d)

#index
print('index')
d = {'key 1':'123','key 2':'value 2', 'key 3':'value 3', 'key 4':'value 4', 'key 5':{'123':[1,2,'drabeMe']}}
print(d['key 5']['123'][2])

#upper
print("UPPER")
d = {'key 1':'123','key 2':'value 2', 'key 3':'value 3', 'key 4':'value 4', 'key 5':{'123':[1,2,'drabeMe']}}
print(d['key 5']['123'][2].upper())

my_stuff = {'lunch':'pizza','breakFast':'idly','dinner':'eggs'}
print(my_stuff['lunch'])
print('reassening the value')
my_stuff['lunch'] = 'biriyani'
print(my_stuff['lunch'])