#연구소
import sys
from collections import deque

rd = lambda : map(int, sys.stdin.readline().split())
wr = sys.stdout

N, M = rd()
arr = [[0]*M for i in range(N)]
eList = list()
vList = list() #바이러스 리스트

for i in range(0,N):
    line = list(rd())
    for j in range(0,M):
        arr[i][j] = line[j]
        if arr[i][j] == 0:
            eList.append([i,j])
        elif arr[i][j] ==2:
            vList.append([i, j])

dir = [[1,0],[-1,0],[0,1],[0,-1]]

def isValid(row,col):
    return row>=0 and col>=0 and row<N and col<M

def bfs():

    visited = [[False]*M for i in range(N)]
    for i in range(0,len(vList)):
        queue = deque([vList[i]])
        visited[vList[i][0]][vList[i][1]] = True #병균 있던 곳
        while queue:
            cur = queue.popleft()

            for j in range(0,len(dir)):
                nextRow = cur[0]+dir[j][0]
                nextCol = cur[1]+dir[j][1]

                if isValid(nextRow,nextCol):
                    if not visited[nextRow][nextCol] and arr[nextRow][nextCol]==0:
                        visited[nextRow][nextCol]=True
                        queue.append([nextRow,nextCol])

    cnt=0
    for i in range(0,N):
        for j in range(0,M):
            if not visited[i][j] and arr[i][j]!=1:
                cnt+=1

    return cnt

maxNum = -1

for i in range (0,len(eList)-2):
    tmp1 = arr[eList[i][0]][eList[i][1]]
    arr[eList[i][0]][eList[i][1]] = 1
    for j in range (i+1, len(eList)-1):
        tmp2 = arr[eList[j][0]][eList[j][1]]
        arr[eList[j][0]][eList[j][1]] = 1
        for k in range(j+1, len(eList)):
            tmp3 = arr[eList[k][0]][eList[k][1]]
            arr[eList[k][0]][eList[k][1]] = 1

            safeArea = bfs()
            maxNum = max(maxNum, safeArea)

            arr[eList[k][0]][eList[k][1]] = tmp3
        arr[eList[j][0]][eList[j][1]] = tmp2
    arr[eList[i][0]][eList[i][1]] = tmp1

wr.write(f"{maxNum}")