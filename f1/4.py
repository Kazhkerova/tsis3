def prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
            if n %i ==0:
                 return False
    return True
def filter(num):
     return[n for n in num if prime(n)]

num_list=list(map(int,input().split()))
res=filter(num_list)
print(res)