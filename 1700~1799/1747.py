#소수&팰린드롬
import sys
N = int(sys.stdin.readline())

arr = [0]*1003002
for i in range(2,len(arr)):
    if arr[i]==0:
        for j in range(i+i,len(arr),i):
            arr[j] = 1

arr[1] = 1

for i in range(N, len(arr)):


    if arr[i]==1:
        continue
    else:
        plus = 1
        if len(str(i))%2==0:
            plus = 0

        if str(i)[:int(len(str(i)) / 2)] == str(i)[int(len(str(i)) / 2) + plus:][::-1]:
            print(i)
            break