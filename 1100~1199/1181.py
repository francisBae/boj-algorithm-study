#단어 정렬
import sys
rd = lambda:sys.stdin.readline()

N=int(rd())

wordList = [[] for i in range(51)]

for i in range(N):
	word=rd().strip()
	wordList[len(word)].append(word)

for i in range(1,51):
	wordList[i].sort()
	prevWord = ""
	for j in range(len(wordList[i])):
		if prevWord == wordList[i][j]:
			continue
		else:
			print(wordList[i][j])
			prevWord = wordList[i][j]
	