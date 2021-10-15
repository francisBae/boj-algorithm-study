#이상한 곱셈
import sys

A,B=sys.stdin.readline().split()

aNum=0
bNum=0
for i in range(len(A)):
	aNum+=int(A[i])

for i in range(len(B)):
	bNum+=int(B[i])

print(aNum*bNum)
		
