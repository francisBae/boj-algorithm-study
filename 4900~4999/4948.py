#베르트랑 공준
import sys
rd = lambda : int(sys.stdin.readline())
limit = 123456*2
prime = [1]*(limit+1)
prime[0]=0
prime[1]=0
for i in range(2,limit+1):
    for j in range(i+i,limit+1,i):
        prime[j] = 0

pCnt = 0
for i in range(limit+1):
    if prime[i]:
        pCnt+=1
    prime[i] = pCnt

while True:
    num = rd()
    if num==0:
        break
    print(prime[2*num]-prime[num])
