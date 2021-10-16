#숫자의 합
import sys
rd=lambda :sys.stdin.readline()
N = int(rd())
numStr = rd()
sum=0
for i in range(N):
    sum+=int(numStr[i])
print(sum)