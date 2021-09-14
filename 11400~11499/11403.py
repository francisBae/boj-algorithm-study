#경로 찾기
import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [[0]*N for i in range(N)]
dict = dict()
answer = [[0]*N for i in range(N)]

for i in range(0,N):
    line = list(map(int, sys.stdin.readline().split()))
    toList = list()
    for j in range(0,N):
        arr[i][j]=line[j]
        if arr[i][j]==1:
            toList.append(j)
    dict[i] = toList #해시맵 + 리스트 형태로 관리

for i in range(0,N):
    visited = [False] * N #다음 경로로 추가했는지 여부 저장
    queue = deque([i])

    while queue:
        next = queue.popleft()
        for j in range(0, len(dict[next])):
            if visited[dict[next][j]] == False:  # 방문 전이라면
                answer[i][dict[next][j]] = 1 # 시작점(i)을 기준으로 갈 수 있는 경로에 1 표시
                queue.append(dict[next][j]) # 큐에 다음 경로 추가
                visited[dict[next][j]] = True # 큐에 추가하면 방문으로 처리

for i in range(0, N):
    for j in range(0, N):
        print(answer[i][j], end=" ")
    print()