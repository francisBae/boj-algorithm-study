#체스
import sys
rd = lambda : list(map(int,sys.stdin.readline().split()))
wr = sys.stdout

N, M = rd()
chessBoard = [[0]*M for i in range(N)]

for i in range(1,4):
    #1 : Queen / 2 : Knight / 3 : Pawn
    line = rd()

    # for j in range(1,1+2*(int(line[0])-1),2):
    for j in range(1,1+line[0]*2,2): #1, 3
        chessBoard[line[j]-1][line[j+1]-1] = i

def isValid(row,col):
    return row>=0 and col>=0 and row<N and col<M

def chkQueen(row,col):
    dir = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[-1,1],[1,1]] #방향

    for i in range(0,len(dir)):
        nextRow = row+dir[i][0]
        nextCol = col + dir[i][1]
        while isValid(nextRow,nextCol):
            if chessBoard[nextRow][nextCol] > 0:
                break
            chessBoard[nextRow][nextCol] = -1
            nextRow = nextRow + dir[i][0]
            nextCol = nextCol + dir[i][1]

def chkKnight(row, col):
    dir = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]] #방향

    for i in range(0,len(dir)):
        nextRow = row+dir[i][0]
        nextCol = col+dir[i][1]

        if isValid(nextRow,nextCol):
            if chessBoard[nextRow][nextCol]==0:
                chessBoard[nextRow][nextCol] = -1

for i in range(0,N):
    for j in range(0,M):
        if chessBoard[i][j] == 1: #queen
            chkQueen(i,j)
        elif chessBoard[i][j] == 2: #knight
            chkKnight(i,j)

answer = 0
for i in range(0,N):
    for j in range(0, M):
        if chessBoard[i][j]==0:
            answer+=1

wr.write(f"{answer}")