#숫자 정사각형
import sys

N,M = map(int,sys.stdin.readline().split())

arr = [[0]*M for _ in range(N)]

for i in range(N):
    line = sys.stdin.readline()

    for j in range(M):
        arr[i][j] = int(line[j])


answer = 1 #정사각형 기본 넓이는 1 (단일 점)

for i in range(N-1):
    for j in range(M-1):
        maxNum = max(i,j)
        for k in range(1, max(N,M)-maxNum):
            if j+k>=M or i+k>=N:
                break
            rightNum = arr[i][j+k]
            downNum = arr[i+k][j]
            rightdownNum = arr[i+k][j+k]

            if arr[i][j] == rightNum == downNum == rightdownNum:
                answer = max(answer,pow(k+1,2))

print(answer)