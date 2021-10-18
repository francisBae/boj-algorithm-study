#단지번호 붙이기
import sys
from collections import deque

rd=lambda:sys.stdin.readline()
N = int(rd())
arr = [[0]*N for i in range(N)]
visited = [[False]*N for i in range(N)]
dir = [[1,0],[-1,0],[0,1],[0,-1]]
areaCnt = [0]*626

for i in range(N):
    line = rd()
    for j in range(N):
        arr[i][j] = int(line[j])

area = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            area+=1
            q = deque()
            q.append([i,j]) #영역 내 시작점
            visited[i][j] = True
            cnt = 1
            #영역별로 큐 수행
            while q:
                point = q.popleft()
                for k in range(4):
                    nRow = point[0]+dir[k][0]
                    nCol = point[1]+dir[k][1]
                    if 0<=nRow<N and 0<=nCol<N and arr[nRow][nCol] and not visited[nRow][nCol]:
                        cnt+=1
                        q.append([nRow,nCol])
                        visited[nRow][nCol]=True
                        arr[nRow][nCol] = area
            areaCnt[area] = cnt

print(area)
answerList = list()
for i in range(1,area+1):
    answerList.append(areaCnt[i])
answerList.sort() #오름차순 정렬
for i in range(len(answerList)):
    print(answerList[i])