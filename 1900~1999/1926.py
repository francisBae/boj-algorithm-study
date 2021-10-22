#그림
import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
arr = [0]*n
for i in range(n):
    arr[i] = list(map(int,sys.stdin.readline().split()))

visited = [[False]*m for i in range(n)]
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
picCnt = 0
answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            picCnt+=1
            sum=1
            q = deque()
            q.append([i,j])
            visited[i][j] = True

            while q:
                point = q.popleft()
                for dir in dirs:
                    nextRow = point[0]+dir[0]
                    nextCol = point[1]+dir[1]
                    if 0<=nextRow<n and 0<=nextCol<m and arr[nextRow][nextCol] and not visited[nextRow][nextCol]:
                        visited[nextRow][nextCol]=True
                        q.append([nextRow,nextCol])
                        sum+=1
            answer = max(answer,sum)

print(picCnt)
print(answer)


