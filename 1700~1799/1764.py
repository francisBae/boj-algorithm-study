#듣보잡
import sys

N, M = map(int,sys.stdin.readline().split())

names = dict()
dbjList = list()

for i in range(N):
    notHeard = sys.stdin.readline().strip()
    names[notHeard] = notHeard

for i in range(M):
    notSeen = sys.stdin.readline().strip()
    if notSeen in names:
        dbjList.append(notSeen)

print(len(dbjList))
dbjList.sort()
for dbj in dbjList:
    print(dbj)