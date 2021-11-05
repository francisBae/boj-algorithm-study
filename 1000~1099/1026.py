#보물
import sys
rd = lambda : sys.stdin.readline()

N = int(rd())
A = list(map(int,rd().split()))
B = list(map(int,rd().split()))

A.sort()
B.sort()
B.reverse()

sum = 0
for i in range(N):
    sum+=A[i]*B[i]

print(sum)