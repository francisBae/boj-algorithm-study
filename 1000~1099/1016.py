#제곱 ㄴㄴ수
import sys,math
minN, maxN = list(map(int,sys.stdin.readline().split()))

minSqrt = 2 #1이 아닌 제곱근
maxSqrt = math.floor(math.sqrt(maxN)) #최대수의 제곱근보다 작거나 같은 정수제곱근
arr = [0]*1000001 #min<=max<=min+1000000

pows = list()
for i in range(minSqrt,maxSqrt+1):
    pows.append(pow(i,2)) #제곱 수들을 저장(4,9,..)

for powN in pows:
    tmp = 0
    if powN>=minN:
        tmp = powN #제곱 수가 min과 동일한 경우
    else:
        tmp = minN+(powN-(minN%powN))%powN #제곱수가 min보다 작으면 min보다 크면서 제곱수로 나뉘는 최소값 구함

    for i in range(tmp-minN,1000001,powN):
        arr[i] = 1 #arr[0]은 min에 대한 인덱스

cnt = 0
for i in range(0, maxN-minN+1):
    if arr[i]==0:
        cnt+=1

print(cnt)
