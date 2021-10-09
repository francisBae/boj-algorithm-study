#약수
import sys
rd = lambda:sys.stdin.readline()
N = int(rd())
divisors = list(map(int, rd().split()))
divisors.sort()
print(divisors[0]*divisors[len(divisors)-1])