#구간 합 구하기 4
import sys

N, M = map(int, sys.stdin.readline().split())


arr = [0]*(N+1)
line = list(map(int, sys.stdin.readline().split()))
arr[1] = line[0]

for i in range(2,N+1):
    arr[i] = line[i-1]+arr[i-1] #이전 수를 더하기

for i in range(0,M):
    fNum, sNum = map(int, sys.stdin.readline().split())

    print(f"{arr[sNum]-arr[fNum-1] }")