#16진수
import sys
hex=sys.stdin.readline().strip()

sum=0
mul=1
for i in range(len(hex)-1,-1,-1):
	if 'A'<=hex[i]<='F':
		sum+=mul*(ord(hex[i])-ord('7'))
	else:
		sum+=mul*int(hex[i])
	mul*=16
print(sum)