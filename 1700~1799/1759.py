#암호 만들기
import sys
rd = lambda : sys.stdin.readline()
L,C=map(int,rd().split())

vowels = dict()
consonants = dict()
alphaStr = list(rd().split())
for i in range(C):
    if alphaStr[i] in ['a','e','i','o','u']:
        vowels[alphaStr[i]] =alphaStr[i]
    else:
        consonants[alphaStr[i]] =alphaStr[i]

alphaStr.sort()

def dfs(codeStr,subAlphaStr,vCnt,cCnt,L):
    # print(codeStr)
    if vCnt+cCnt==L:
        if vCnt>=1 and cCnt>=2:
            print(codeStr)
        else:
            return

    for i in range(len(subAlphaStr)):
        localVCnt = vCnt
        localCCnt = cCnt
        ch = subAlphaStr.pop(i)
        if ch in vowels:
            localVCnt += 1
        else:
            localCCnt += 1
        subAlphaStr.insert(i, ch)
        dfs(codeStr+str(ch), subAlphaStr[i+1:], localVCnt, localCCnt, L)



for i in range(C-L+1):
    vCnt = 0
    cCnt = 0
    ch = alphaStr.pop(i)
    if ch in vowels:
        vCnt+=1
    else:
        cCnt+=1
    alphaStr.insert(i,ch)
    dfs(str(ch),alphaStr[i+1:],vCnt,cCnt,L)
    # print(alphaStr)