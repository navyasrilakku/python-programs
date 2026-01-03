a=int(input())
b=int(input())
try:
	print("connecting database")
	c=a//b
	print(c)
except Exception as e:
	print(e)
	print("disconnecting database")
	