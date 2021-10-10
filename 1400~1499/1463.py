#1로 만들기
import sys
N = int(sys.stdin.readline())
arr = [0]*1000001

arr[2] = 1
arr[3] = 1

for i in range(4,1000001):
    if i%3==0:
        arr[i] = min(arr[i//3]+1,arr[i-1]+1)
        if i%2==0: #2로 나눈 경우도 체크
            arr[i] = min(arr[i],arr[i//2]+1)
    elif i%2==0:
        arr[i] = min(arr[i//2]+1,arr[i-1]+1)
    else:
        arr[i] = arr[i-1]+1

print(arr[N])