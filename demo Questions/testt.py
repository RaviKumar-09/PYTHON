class A:
        def m1(self):
                print('A class method')
class B:
        def m1(self):
                print('B class method')
class C:
        def m1(self):
                print('C class method')
class X(A,B):
        def m1(self):
                print('X class method')
class Y(B,C):
        def m1(self):
                print('Y class method')
class P(X,Y):
        def m1(self):
                print('Z class method')
p = P()
p.m1()


