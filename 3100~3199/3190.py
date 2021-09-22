#뱀
import sys
rd = lambda : int(sys.stdin.readline())
rd2 = lambda : list(map(int,sys.stdin.readline().split()))

N = rd() #보드 크기 N
K = rd() #사과의 위치 K개

arr = [[0]*N for i in range(N)]

arr[0][0] = -1 #최초 뱀의 위치

for _ in range(K):
    line = rd2()
    arr[line[0]-1][line[1]-1] = 1 #사과 위치는 1로 표시

L = rd() #방향전환 수

chgDir = dict()
for i in range(L):
    line = list(sys.stdin.readline().split())
    # chgDir[i] = list(sys.stdin.readline().split())
    chgDir[int(line[0])] = line[1]
# print(chgDir)

up = [-1,0]
down = [1,0]
right = [0,1]
left = [0,-1]
curDir = right #최초 R방향 이동

def getNextDir(dirChar):
    #L : 왼쪽, D : 오른쪽
    nextDir = curDir
    if curDir==up:
        if dirChar=='L':
            nextDir = left
        else:
            nextDir = right
    elif curDir==down:
        if dirChar=='L':
            nextDir = right
        else:
            nextDir = left
    elif curDir==right:
        if dirChar=='L':
            nextDir = up
        else:
            nextDir = down
    else:
        if dirChar=='L':
            nextDir = down
        else:
            nextDir = up
    return nextDir

sec = 0 #초
nextRow = 0 #최초이동
nextCol = 1 #최초이동

snakeList = list()
snakeList.append([0,0]) #최초 위치 등록 / 사과 못 먹었을 때 지우기 위함



while True:
    sec += 1
    if 0<=nextRow<N and 0<=nextCol<N:
        # print(snakeList)
        if arr[nextRow][nextCol]==-1:
            break


        if arr[nextRow][nextCol]==1: #사과냠냠
            snakeList.append([nextRow,nextCol])

        else:

            snakeList.append([nextRow,nextCol])
            arr[snakeList[0][0]][snakeList[0][1]] = 0
            snakeList.pop(0) #꼬리 줄이기

        arr[nextRow][nextCol] = -1 #뱀의 머리
        # print(sec)
        # for i in range(N):
        #     for j in range(N):
        #         print(arr[i][j],end=' ')
        #
        #     print()

        if sec in chgDir:
            curDir = getNextDir(chgDir[sec])
        nextRow = nextRow+curDir[0]
        nextCol = nextCol + curDir[1]

    else:
        break

print(sec)

