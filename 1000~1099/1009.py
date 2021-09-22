#분산처리
import sys

endNum = list()
endNum.append([10])
endNum.append([1])
endNum.append([2,4,8,6])
endNum.append([3,9,7,1])
endNum.append([4,6])
endNum.append([5])
endNum.append([6])
endNum.append([7,9,3,1])
endNum.append([8,4,2,6])
endNum.append([9,1])

T = int(sys.stdin.readline())

for _ in range(T):
    line = list(map(int,sys.stdin.readline().split()))

    line[0]=line[0]%10
    print(endNum[line[0]][((line[1])%len(endNum[line[0]])-1)%len(endNum[line[0]])])