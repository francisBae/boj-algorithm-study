#손익분기점
import sys,math
A,B,C = map(int,sys.stdin.readline().split())
if C-B==0:
    print(-1)
else:
    answer = int(math.floor(A/(C-B))+1)
    if answer<0:
        answer = -1
    print(answer)