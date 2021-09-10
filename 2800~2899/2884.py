#알람 시계
import sys

H, M = map(int,sys.stdin.readline().split()) #Hour Minute
if M<45:
    H = (H-1)%24
M = (M-45)%60
print(f"{H} {M}")