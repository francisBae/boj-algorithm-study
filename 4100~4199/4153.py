#직각삼각형
import sys

while True:
    nums = list(map(int,sys.stdin.readline().split()))
    nums.sort()
    if nums[0]==0:
        break
    elif pow(nums[0],2)+pow(nums[1],2)==pow(nums[2],2):
        print("right")
    else:
        print("wrong")