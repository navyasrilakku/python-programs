
r=5
for i in range(r+1,0,-1):
    for j in range(0,i-1):
        if i<j:
            print(" ",end=' ')
        else:
            print(j,end="    ")
    print(" ")
'''def  max_seq(N,k,prices):
    max_len=0
    cur_len=0
    cur_sum=0
    left,right=0,0
    while right<N:
        cur_sum+=prices[right]
        while cur_sum>=k:
            cur_sum-=prices[left]
            left+=1
        cur_len= right-left+1
        max_len=max(max_len,cur_len)
        right+=1
    return max_len
N=int(input())
k=int(input())
prices=list(map(int,input().split()))
res = max_seq(N,k,prices)
print(result)'''

    
