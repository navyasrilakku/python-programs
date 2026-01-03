import re
pwd=input("Enter pass:   ")
plen=len(pwd)
isval=False

while True:
    if plen<7 and plen>20:
        break
    elif not re.search('[A-Z]',pwd):
        break
    elif not re.search('[a-z]',pwd):
        break
    elif not re.search('[0-9]',pwd):
        break
    elif not re.search('[$#@!.,*]',pwd):
        break
    elif re.search('\s',pwd):
        break
    else:
        isval=True
        break
if isval:
    print("val")
else:
    print("not val")
    
    
