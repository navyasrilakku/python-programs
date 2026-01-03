class A:
    def display(self):
        print("A")
class B:
    def display(self):
        print("B")
class C(A,B):
    def display(self):
        print("C")
c=C()
c.display()
c.display()
