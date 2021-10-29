#진짜 공간
import sys,math
rd = lambda : sys.stdin.readline()
N = int(rd())
line = list(map(int,rd().split()))
cluster = int(rd())

sum = 0
for i in range(N):
    sum+=cluster*math.ceil(line[i]/cluster)

print(sum)


