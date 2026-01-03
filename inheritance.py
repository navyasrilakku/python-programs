class A:
    def displaya(self):
        print("classs a method")
class B(A):
    print("B")
class C(A):
    def displayc(self):
        print("classs c method")

c=C()
a=A()
b=B()
b.displaya()
c.displayc()
a.displaya()
c.displaya()
