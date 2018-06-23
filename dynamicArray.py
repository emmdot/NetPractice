import sys

logistics = list(map(int,raw_input().split()))
par1 = logistics[0]
par2 = logistics[1]
seqList = []
lastAnswer = 0
for i in xrange(par2):
	seqList.append(map(int,raw_input().strip().split(' ')))

print type(seqList)

for j in seqList:
	print seqList


