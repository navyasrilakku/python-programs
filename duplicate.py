s=input()
str=""
l=[]
for i in s:
    if i not in l:
        l.append(i)
print("".join(l))
