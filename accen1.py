'''arr=[12,25,43,68,18,24]
count=0
for i in range(len(arr)):
    if(arr[i]%2==0 and arr[i]%6==0):
        count+=arr[i]
print(count)'''


'''a=41261
b=4861
c=6521
count=0
s="".join(str(a)+str(b)+str(c))
for i in s:
    if s.count(i)>count:
        count=s.count(i)
        ch=i
print(ch)'''



'''k=input()
if(len(k))<8:
    print("Invalid")
else:
    u,l,d,s=0,0,0,0
    for i in k:
        if i.isupper():

            u=1
        if i.islower():
            l=1
        if i.isdigit():
            d=1
        if(ord(i) in range(33,64)):
            s=1
    if u==1 and l==1 and d==1 and s==1:
        print("valid")
    else:
        print("Invalid")'''



'''s=input()
k=[]
for i in range(len(s)):
    if(s[i].isdigit()):
        k.append(s[i])
    else:
        print(s[i],end="")'''




'''n=[18,19,18,19,3]
k={}
for i in n:
    if i in k:
        k[i]+=1
    else:
        k[i]=1
count=[i for i, c in k.items() if c>1]
print(len(count))'''




'''def check(num):
    num=str(num)
    twos=num.count('2')
    ei=num.count('8')
    fo=num.count('4')
    return twos==ei==fo and twos>0
def count_nums(n):
    count=0
    for i in range(1,n+1):
        if(check(i)):
            count+=1
    return count%1000000007
n=int(input())
print(count_nums(n))'''




'''s='1A0B1B1A0C1'
res=int(s[0])
for i in range(0,len(s),2):
    if(s[i]=='A'):
        res=res & int(s[i])
    if(s[i]=='B'):
        res=res | int(s[i])
    if(s[i]=='C'):
        res=res ^ int(s[i])
print(res)'''


'''input:-s= he is playing foot ball and he is summing and enjoying the summer.
output:- he is playing football and summing enjoying the summer.'''
'''
input :- amaama
output- palindrome and symmetric
input:-s="kitaatik"
output:-print("not symmetric")
        print("palind")'''



'''s="he is playing football and he is summing and enjoying the summer"
k=s.split(" ")
l=[]
for i in k:
    if i not in l:
        l.append(i)
print(" ".join(l))'''


s="kitaatik"
k=s[::-1]
m=s[:len(s)//2:]
d=s[len(s)//2:len(s):]

if(s==k):
    if(m==d):
        print("symmetrical palind")
    else:
        print("not symmetric")
        print("palind")
else:
    print("not palind")

    
    
    
    






