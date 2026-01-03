class A:
	def method():
		print("A")
class B:
	def method():
		print("B")
class C(A,B):
	pass
c=C()
print(C.__mro__)
	