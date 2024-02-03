def r():
    s=input()
    words=s.split()
    rev=' '.join( reversed(words))
    return rev
res=r()
print(res) 