class A:
    def display(self):
        print("A")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
d=D()
print(D.__mro__)
d.display()
