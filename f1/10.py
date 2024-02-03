def palindrome(word):
    return word == word[::-1]
n=list(map(str,input().split()))
res=palindrome(n)
print(res)