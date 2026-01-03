l=list(map(int,input().split()))
l1=[]
temp=0
for i in l:
	for j in range(int(i+1),l):
		l[i]=temp
		l[j]=l[i]
		l[j]=temp
		i=i+2
		j=j+2
print(l1.append(l[i,j]))