#직사각형에서 탈출
import sys

x,y,w,h = map(int,sys.stdin.readline().split())
minW = min(abs(x),abs(w-x))
minH = min(abs(y),abs(h-y))
print(min(minW,minH))