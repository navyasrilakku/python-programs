s=input()
s=s.lower()
s=s.split()
al="abcdefghijklmnopqrstuvwxyz"
res=""
for i in s:
    sum=0
    m=0
    n=len(i)-1
    for j in range(0,len(i)):
        if i[j] in al:
            if m<n:
                sum=sum+abs((al.index(i[m])+1)-(al.index(i[n])+1))
                m+=1
                n-=1
                if m>n:
                            break
            else:
                sum=sum+al.index(i[n])+1
                break
    res=res+str(sum)
print(res)
                
