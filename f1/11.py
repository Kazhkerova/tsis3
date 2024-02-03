def histogram(numbers):
    for num in numbers:
        print('*' * num)
num_list=list(map(int,input().split()))
res=histogram(num_list)
print(res)
 