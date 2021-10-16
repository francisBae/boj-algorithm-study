#X보다 작은 수
import sys

rd = lambda : map(int,sys.stdin.readline().split())
N,X=rd()
nums = list(rd())

numList = list()
for num in nums:
    if num<X:
        numList.append(num)
print(*numList)