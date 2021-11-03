#베스트셀러
import sys

rd=lambda:sys.stdin.readline()
N=int(rd())

strDict = dict()
strList = list()

answer = 1

for _ in range(N):
	line = rd().strip()
	if line in strDict:
		strDict[line] = strDict[line]+1
			
		answer = max(answer,strDict[line])
	else:
		strDict[line] = 1

for st in strDict:
	if strDict[st]==answer:
		strList.append(st)		
strList.sort()
print(strList[0])