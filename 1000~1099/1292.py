#쉽게 푸는 문제
import sys

arr = [0]*500501 #1~1000
A,B = map(int,sys.stdin.readline().split())

cur = 1
for i in range(1001):
    for j in range(cur,cur+i):
        arr[j]=i
    cur = cur+i

sum=0
for i in range(A,B+1):
    sum+=arr[i]

print(sum)