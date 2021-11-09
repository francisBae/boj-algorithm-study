#홀수일까 짝수일까
import sys
rd = lambda:int(sys.stdin.readline())

N=rd()
for _ in range(N):
	K = rd()
	if K%2==1:
		print("odd")
	else:
		print("even")
