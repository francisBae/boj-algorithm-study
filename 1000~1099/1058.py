import sys

rd = lambda: sys.stdin.readline()
N = int(rd())
link = ['N'] * N
for i in range(N):
    link[i] = rd().strip()

answer = -1
for i in range(N): #i : 시작점
    numDict = dict()
    for j in range(N): #j : 1차 방문 노드
        if link[i][j] == 'Y':
            if j not in numDict:
                numDict[j] = j
            for k in range(N): #k : 2차 방문 노드
                if link[j][k] == 'Y':
                    if k not in numDict and k != i: #2차 방문 후 자신을 방문할 수는 없음
                        numDict[k] = k
    answer = max(answer, len(numDict))
print(answer)