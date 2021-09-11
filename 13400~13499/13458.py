#시험 감독
import sys, math

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int,sys.stdin.readline().split())

cnt=0

for i in range(0, len(A)):
    cnt+=1 #총감독은 무조건 1명 존재
    A[i]-=B #총감독이 보는 학생 제외
    if A[i]>0:
        cnt+=math.ceil(A[i]/C)
print(f"{cnt}")