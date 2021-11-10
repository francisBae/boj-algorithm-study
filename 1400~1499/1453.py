#피시방 알바
import sys

PC = [0]*101
N = int(sys.stdin.readline())
guest = list(map(int,sys.stdin.readline().split()))

cnt = 0
for i in range(N):
    if PC[guest[i]]:
        cnt+=1
    else:
        PC[guest[i]]=1

print(cnt)