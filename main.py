from math import factorial
nk=input().split()
n=int(nk[0])
k=int(nk[1])
newton=int((factorial(n)/(factorial(k)*factorial(n-k))))
print(newton)
