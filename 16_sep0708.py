'''from itertools import combinations
lst=['1010','0100','0001','1111','1011']
val=[10,4,1,15,11]
l1=[]
l2=[]
l3=[]
for i in range(1,len(lst)):
    l1.extend(list(combinations(lst,i)))
for i in l1:
    if(len(i)==1):
        if(i[0]=='1111'):
            l2.append(list(i))
    else:
        sum=0
        for j in i:
            sum=sum+int(j,2)
        if(sum==15):
            l2.append(list(i))
if(len(l2)==0):
    print(-1)
else:
    for i in l2:
        sum=0
        for j in i:
            ind=lst.index(j)
            sum=sum+val[ind]
        l3.append(sum)
    print(min(l3))'''









'''def min_ar(a,n,min_n):
    res=[]
    for i in range(len(n)):
        for j in range(0,i+1):
            if(i==j):
                b=n[i]-a[j]
                res.append(b)
    max_res=max(res)
    c=min_n-max_res
    return c
s=int(input())
s1=[int(x) for x in input().split()]
s2=[int(x) for x in input().split()]
min_s2=min(s2)
while len(s2)<len(s1):
    s2.append(0)
out=min_ar(s1,s2,min_s2)
print(out)'''










'''num=int(input())
str=input()[:num]
l=[]
l1=[]
res=[]
num_pair=int(input())
for i in range(num_pair):
    pair=input()
    n1,n2=map(int,pair.split())
    l.append(n1,n2)
for i in l:
    left=i[0]
    right=i[len(i)-1]
    palind=string[left-1:right]
    if palindrome[::-1]==palindrom:
        res.append(0)
    else:
        if len(palind)==3:
            for i in range(0,len(palind)):
                p=palind[i+1:]+palind[i]
            if p==p[::-1]:
                res.append(0)
                break
        else:
            for j in palind:
                t= palind.replace(j,input())
                if t==t[::-1]:
                    res.append(1)
                    break
                else:
                    b=palind.replace(j,'')
                    if b==b[::-1]:
                        res.append(1)
                        break
print(res)'''

            
