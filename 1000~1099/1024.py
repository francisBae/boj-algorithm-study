#수열의 합
import math
import sys

N, L = map(int, sys.stdin.readline().split())

numList = list()

for i in range(L, 101):

    mid = math.ceil(N/i)

    #n(n+1)/2 - m(m+1)/2 원리 이용
    n = mid + math.ceil(i / 2) -1
    m = mid-int(i/2)

    if m<0:
        break

    sum = int((n * (n + 1) - (m - 1) * m) / 2)

    if sum == N:
        for j in range(m, n+1):
            numList.append(j)
        break

if len(numList)==0:
    numList.append(-1)

print(*numList)