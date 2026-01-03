n=int(input())
l2=[]
l3=[]
l4=[]
s=str(n)
s1=sorted(s)
l=list(s1)
for i in l:
    if i not in l3:
        l3.append(i)
for i in l3:
    s2=l.count(i)
    l2.append(s2)


if(len(l)!=len(l2)):
    l2.append(0)
if(l==l2):
    for  i in l:
        if i not in l4:
            l4.append(i)
    print(l4)
else:
    print("0")

