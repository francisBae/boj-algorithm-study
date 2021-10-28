#단어 공부
import sys
alpha = [0]*26
line = sys.stdin.readline().strip().lower()
maxList = list()
maxNum = 0
for i in range(len(line)):
    idx = ord(line[i])-ord('a')
    alpha[idx]+=1

    maxNum = max(maxNum,alpha[idx])

cnt=0
maxIdx = -1
for i in range(len(alpha)):
    if alpha[i]==maxNum:
        cnt+=1
        maxIdx = i

if cnt>1:
    print("?")
else:
    print(chr(maxIdx+ord('A')))