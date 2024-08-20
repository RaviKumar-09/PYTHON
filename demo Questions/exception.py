# Exception Handling
print('Exception Handling')
class Join:
    def __init__(self):
        print("constructor")
    def welocme (self):
        print("welocme")
    def __del__(self):
        print('destructor')
    def members(self):
        members = ["chinnari","ravi","amma"]
        print(members[1])

j1 = Join()
j1.wlocome()
j1.members()