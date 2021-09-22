#감시
import sys

class CCTV:
    def __init__(self,num,row,col,type,idx):
        self.num = num
        self.row = row
        self.col = col
        self.type = type
        self.idx = idx
    def __str__(self):
        return "["+str(self.num)+","+str(self.row)+","+str(self.col)+","+str(self.type)+","+str(self.idx)+"]"

rd = lambda : map(int,sys.stdin.readline().split())

N, M = rd()

cctvList = list()
cctvCnt = 0
wallCnt = 0

arr = [[0]*M for i in range(N)]
for i in range(N):
    line = list(rd())
    for j in range(M):
        arr[i][j] = line[j]
        if 0<arr[i][j]<6:

            cctvList.append(CCTV(arr[i][j],i,j,-1,cctvCnt))
            cctvCnt += 1

up = [-1,0]
down = [1,0]
left = [0,-1]
right = [0,1]

cctvType = list()
cctvType.append([]) #빈 리스트
cctvType.append([[up],[down],[left],[right]]) #case 1 상 or 하 or 좌 or 우
cctvType.append([[up,down],[left,right]]) #상하 or 좌우
cctvType.append([[up,right],[right,down],[down, left],[left,up]]) #상우 or 우하 or 하좌 or 좌상
cctvType.append([[left,up,right],[up,right,down],[right,down,left],[down,left,up]]) #ㅗ ㅏ ㅜ ㅓ
cctvType.append([[up,down,left,right]])

def dfs(curIdx):
    if curIdx >= cctvCnt: #cctv 모두 확인 => 검색 시작
        # print(*cctvList)

        visited = [[False]*M for _ in range(N)]

        for i in range(0, N):
            for j in range(0, M):
                curNum = arr[i][j]
                if curNum>0:
                    visited[i][j] = True

        for cctv in cctvList:
            for type in cctvType[cctv.num][cctv.type]:

                nextRow = cctv.row + type[0]
                nextCol = cctv.col + type[1]

                while 0 <= nextRow < N and 0 <= nextCol < M:
                    if arr[nextRow][nextCol] == 6:
                        break
                    visited[nextRow][nextCol] = True
                    nextRow = nextRow + type[0]
                    nextCol = nextCol + type[1]
        cnt = 0
        for i in range(0, N):
            for j in range(0, M):
                if visited[i][j]==False:
                    cnt+=1

        return cnt

    answer = sys.maxsize
    tmpNum = answer

    for i in range(len(cctvType[cctvList[curIdx].num])):
        tmpType = cctvList[curIdx].type
        cctvList[curIdx].type = i #cctvType[i]

        tmpNum=dfs(curIdx+1)

        cctvList[curIdx].type = tmpType

        if tmpNum<answer:
            answer = tmpNum

    return answer

answer = dfs(0)

print(answer)
