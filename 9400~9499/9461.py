#파도반 수열
import sys

rd = lambda : int(sys.stdin.readline())

P = [0]*101
P[1] = 1
P[2] = 1
P[3] = 1

for i in range(4,101):
    P[i] = P[i-2]+P[i-3]

T = rd()

for _ in range(T):
    N = rd()
    print(P[N])