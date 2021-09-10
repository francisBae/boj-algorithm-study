#피보나치 수열
import sys

input = sys.stdin.readline()

fibo = [[0]*2 for i in range(41)] #피보나치
fibo[0][0] = 1 #fibo(0) : 0 1
fibo[0][1] = 0
fibo[1][0] = 0 #fibo(1) : 1 0
fibo[1][1] = 1

for i in range(2, len(fibo)):
    for j in range(0, len(fibo[0])):
        fibo[i][j] = fibo[i-1][j]+fibo[i-2][j]

for iter in range(0, int(input)):
    num = int(sys.stdin.readline())
    fibo0 = fibo[num][0]
    fibo1 = fibo[num][1]
    print(f"{fibo0} {fibo1}")