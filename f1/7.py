def spy_game(n):
    for i in range(len(n) - 2):
        if n[i] == 0 and n[i+1] == 0 and n[i+2]==7:
            return True
    return False
num_list=list(map(int,input().split()))
res=spy_game(num_list)
print(res)