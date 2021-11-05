#8진수 2진수
import sys

octal = ["000"
         ,"001"
         ,"010"
         ,"011"
         ,"100"
         ,"101"
         ,"110"
         ,"111"]

numStr = sys.stdin.readline().strip()
answer=""

if int(numStr)==0:
    answer+="0"
else:
    for i in range(len(numStr)):
        answer+=octal[int(numStr[i])]

    answer = answer.lstrip("0")
print(answer)









