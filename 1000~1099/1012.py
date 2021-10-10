#유기농 배추
import sys
sys.setrecursionlimit(2503) #재귀한도 임의 설정(50*50+@ 인듯)
rd = lambda:sys.stdin.readline()
T = int(rd())
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
arr = []
visited = []

def dfs(area,curRow,curCol,N,M):

    for dir in dirs:
        newRow = curRow+dir[0]
        newCol = curCol+dir[1]

        if 0<=newRow<N and 0<=newCol<M:
            if not visited[newRow][newCol] and arr[newRow][newCol]==1:
                visited[newRow][newCol] = True
                arr[newRow][newCol] = area
                dfs(area,newRow,newCol,N,M)

for i in range(T):
    M,N,K = map(int,rd().split())
    area = 0
    arr = [[0]*M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for j in range(K):
        X,Y = map(int, rd().split())
        arr[Y][X] = 1

    for row in range(N):
        for col in range(M):
            if not visited[row][col] and arr[row][col]==1:
                area+=1 #구역마다 번호 붙이는 용도. 최종 구역은 제일 높은 수
                visited[row][col] = True
                arr[row][col] = area
                dfs(area,row,col,N,M)
    print(area)