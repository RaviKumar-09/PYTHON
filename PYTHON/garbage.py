# how to enable and disable garbage collector in the python.
"""import gc
class Test:
	print(gc.isenabled())
	gc.disable()
	print(gc.isenabled())
	gc.enable()
	print(gc.isenabled())"""


"""import time
class Test:
	def__init__(self):
		print('Oject Initialization....')
	def__del__(self):
		print('Fullfilling last wish and performaing clean upm activites...')
t = Test()
t = None
time.sleep('10')
print('End of applications')"""

"""import time
class Test:
   def__init__(self):
	 print('Constructor Execution'...)
   def__del__('self'):
	 print('Destructor Execution')
list = [Test(),Test(),Test()]
del list
time.sleep(5)
print('End of the applications')"""


"""name = input("Enter a Name")
if name== 'ravi':
	print("hellow ravi how are you")
print("what are you doing")"""

""""
class Bottle:
    id=1
    color = 'red'
    capacity = 1
    height = 30
    
    
    def wash():
        print('washing')
    
    def setcap():
        print('setting cap')
        
    def fillwater():
        print('fill water')"""
"""
def addAll(a,b):
	return a+b


numbers =[10,1,3,10,5]
result = reduce(addAll,numbers,10)
print(result)"""


friends = ['jenny','marry','loggy']
result = map(lamda ,namen,name.upper(),friends)
print(list(result))