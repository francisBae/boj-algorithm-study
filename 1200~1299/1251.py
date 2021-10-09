#단어 나누기
import sys

word = sys.stdin.readline().strip()
wordList = list()

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        front = word[:i]
        mid = word[i:j]
        rear = word[j:]

        wordList.append(front[::-1]+mid[::-1]+rear[::-1])

wordList.sort()
print(wordList[0])
