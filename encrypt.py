def CustomCaesarCipher(key,msz):
    m=[]
    for i in msz:
        if((i>='A' and i<='Z')or(i>='a'and i<='z')):
            v=chr(ord(i)+key)
            m.append(v)
        else:
            m.append(i)
    print("".join(m))
key=int(input())
msz=input()
CustomCaesarCipher(key, msz)
        
        
        
