#골드바흐의 추측
import sys
rd = lambda:int(sys.stdin.readline())

arr = [1]*1000001
arr[0] = 0
arr[1] = 0
for i in range(2,1000001):
    for j in range(i+i,1000001,i):
        arr[j] = 0

while True:
    n = rd()

    if n==0:
        break

    isPrime = False
    for i in range(2,n):
        if arr[i] and arr[n-i]:
            isPrime = True
            print(str(n)+" = "+str(i)+" + "+str(n-i))
            break

    if not isPrime:
        print("Goldbach's conjecture is wrong.")