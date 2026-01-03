s=input().lower()
res=""
for i in s:
    if(i.isalnum()):
        res+=i
if(res[::-1]==res):
    print("true")
else:
    print("false")
