def unique(l):
    return list(dict.fromkeys(l))
n=list(map(str,input().split()))
res=unique(n)
print(res)