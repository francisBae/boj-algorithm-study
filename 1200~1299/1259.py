#팰린드롬수
import sys

while True:
    num = sys.stdin.readline().strip()
    if int(num) == 0:
        break

    length = len(num)
    if length%2==0:
        if num[0:length//2] == num[length//2:][::-1]:
            print("yes")
        else:
            print("no")
    else:
        if num[0:length//2] == num[length//2+1:][::-1]:
            print("yes")
        else:
            print("no")