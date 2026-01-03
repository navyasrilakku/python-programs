n=int(input())
l2=[]
count=0
l3=[]
s=str(n)
s1=sorted(s)
l=list(s1)
for i in l:
    if i not in l3:
        l3.append(i)
for i in l3:
    s2=l.count(i)
    l2.append(s2)
print(l2)
