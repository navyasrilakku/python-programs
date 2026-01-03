n=int(input())
temp=n
l=len(str(n))
sum=0
while(n>0):
    rem=n%10
    sum=sum+pow(rem,l)
    n=n//10
if(temp==sum):
    print("armstrong number")
else:
    print("not armstrong number")
