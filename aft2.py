def smallsub(arr,n,k):
    min_len=float('inf')
    bitwise_or=0
    left=0
    for right in range(n):
        bitwise_or |= arr[right]
        while bitwise_or>=k:
            min_len = min(min_len,right-left+1)
