#수 찾기
import sys
rd = lambda : sys.stdin.readline()

N = int(rd())

line = list(map(int, rd().split()))
numDict = dict()

for num in line:
    numDict[num] = num

M = int(rd())
line2 = list(map(int, rd().split()))

for num in line2:
    print(1) if num in numDict.keys() else print(0) #삼항연산자