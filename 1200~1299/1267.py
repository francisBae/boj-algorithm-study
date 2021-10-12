#핸드폰 요금
import sys
rd=lambda:sys.stdin.readline()

N = int(rd())
line = list(map(int,rd().split()))

Y=0
M=0
for i in range(N):
	Y+=10*(line[i]//30)+10
	M+=15*(line[i]//60)+15

answer = list()
if Y<M:
	answer.append('Y')
	answer.append(Y)
elif Y>M:
	answer.append('M')
	answer.append(M)
else:
	answer.append('Y')
	answer.append('M')
	answer.append(Y)
print(*answer)