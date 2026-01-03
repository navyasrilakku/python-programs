a=int(input())
b=int(input())
try:
	c=a//b
	print(c)
except ZeroDivisionError as e:
	print(e)
print("Hello")