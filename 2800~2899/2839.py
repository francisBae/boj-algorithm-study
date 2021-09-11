#설탕 배달
import sys

N = int(sys.stdin.readline())

cnt = 0
while(N>0):
    if N%5==0: #5로 나눌 수 있는 수인지 확인
        cnt+=N/5
        break
    else:
        N-=3 #나눌 수 없으면 3을 빼고 다시 진행
        cnt+=1
    if N<0: #더 이상 수행 불가
        cnt=-1
        break
print(f"{int(cnt)}")