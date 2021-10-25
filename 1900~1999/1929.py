#소수 구하기
import sys
M,N = map(int,sys.stdin.readline().split())

arr = [1]*1000001
arr[0] = 0
arr[1] = 0
for i in range(2,len(arr)):
    for j in range(i+i,len(arr),i):
        arr[j] = 0

for i in range(M,N+1):
    if arr[i]:
        print(i)