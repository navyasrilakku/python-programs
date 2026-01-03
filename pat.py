n=int(input())

for i in range(1,n+1):
    l=[]
    
    for j in range(1,i+1):
        if j==1:
            print(n,end=" ")
        elif j==2:
            print(n+(n-1),end=" ")
            l.append(n)
            l.append(n+(n-1))
        else:
            print(sum(l),end=" ")
            l.append(sum(l))
    print()
