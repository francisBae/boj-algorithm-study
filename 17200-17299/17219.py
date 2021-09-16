#비밀번호 찾기
from sys import stdin,stdout

rd = lambda:stdin.readline()
wr = stdout.write

N,M = map(int, rd().split())

account = dict()
for i in range(0, N):
    id, pw = rd().split()
    account[id] = pw

for i in range(0, M):
    id = rd().rstrip() #끝의 개행문자 제거
    print(f"{account[id]}")