#최대 곱
import sys
S,K = map(int,sys.stdin.readline().split())
num = int(S/K)
mod = S-num*K

mul=1
for i in range(0,K):
    if i<mod:
        mul*=(num+1)
    else:
        mul*=num
print(mul)