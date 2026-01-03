v=int(input())
w=int(input())
for i in range(1,v):
    if w%2==0 or v<w or 2<=w:
        tw= (2*v-w)/2
        k=abs(tw)
        fw= v-k
    else:
        print("Invalid input")
print(k," two wheel")
print(fw,"four wheel")
