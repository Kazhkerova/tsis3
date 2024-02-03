def solve(heads, legs):
    chiken=(4*heads-legs)/2
    rab=heads-chiken
    return int(chiken), int(rab)
h=int(input())
l=int(input())
res=solve(h,l)
print(res)
