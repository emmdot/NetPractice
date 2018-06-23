import math

n=int(raw_input())
seq = list(map(int,raw_input().rstrip().split(' ')))
for i in seq:
	x = seq.count(i)
	if x == 1:
		print i


