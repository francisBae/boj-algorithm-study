#소수
import sys

rd =lambda:int(sys.stdin.readline())
prime =[1]*10001
prime[0]=0
prime[1]=0

M=rd()
N=rd()

for i in range(2,10001):
	for j in range(i+i,10001,i):
		prime[j]=0

answer=-1
sum=0
for i in range(M,N+1):
	if prime[i]==1:
		if answer==-1:
			answer=i
		sum+=i

if sum>0:
	print(sum)
print(answer)