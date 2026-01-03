s=input()
s1=input()
i=0
j=0
res=""
if len(s)==len(s1):
    for k in range (0,len(s1)):
            res=res+s[i]+s1[j]
            i+=1
            j+=1
print(res)
            
