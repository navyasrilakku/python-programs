s=input()
re=[]
re.append(sum([int(i) for i in s]))
re.append(int(s))
for i in range(len(s)):
    if i!=0:
        re.append(int(s[0:i])+int(s[i:]))
print(sum(re))
