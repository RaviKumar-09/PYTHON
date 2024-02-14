'''import review
print('I am the final program')

print(__name__)
def main() :
    print('entry point')'''
    
'''if(__name__=="__main__"):
    main()''' 
    
    
'''print("welcome to my house")

def welcome():
    print('welocme to python programing language')
def subscribe():
    print('ravi to our one and only good man')
welcome()'''

'''with open('ifstatements.txt' , 'r') as file:
    print(file.read())'''
''' 
class Bottle:
    id=1
    color = 'red'
    capacity = 1
    height = 30
    
    
    def wash():
        print(washing)
    
    def setcap():
        print('setting cap')
        
    def fillwater():
        print('fill water')'''
        
        
class Employee:
    def_init_(self,eno,ename,eaddr):
      self.eno = eno
      self.ename = ename
      self.eaddr = eaddr
    def display(self):
      print(self.eno,'\t',self.ename,'\t'.self.eaddr)
with open('emp.dat','sunny','Mumbai')
  e = Employee(101,'Sunny','Mumbai')
  pickle.dump(e,f)
  print('Pickling of employee object completed...')
with open('emp.dat','rb')as f:
  obj = pickle.load(f)
  print('printing employeeinfo after unpikling')
  obj.display()
