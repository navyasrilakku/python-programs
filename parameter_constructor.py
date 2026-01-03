class Greeks:
    f=0
    s=10
    a=0
    def __init__(self,f,s):
        self.f=f
        self.s=s
    def display(self):
        print(str(self.f))
        print(str(self.s))
        print(str(self.a))
    def cal(self):
        self.a=self.f+self.s
obj1=Greeks(100,200)
