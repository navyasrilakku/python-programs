'''n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)+1):
        l1.append(list(l[i:j]))
for i in l1:
    if sum(i)<=k:
        l2.append(len(i))

print(max(l2))'''
row=6
for r in range(1,row):
    n=1
    for j in range(row,0,-1):
        if j>r:
            print(" ",end=' ')
        else:
            print(n,end="    ")
            n+=1
    print(" ")

