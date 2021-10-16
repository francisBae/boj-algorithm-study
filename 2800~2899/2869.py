#달팽이는 올라가고 싶다
import sys,math
A,B,V = map(int,sys.stdin.readline().split())

if A>V:
    print(1)
else:
    day = int(math.ceil(1+(V-A)/(-B+A)))
    print(day)