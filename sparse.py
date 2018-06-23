import sys

n = int(raw_input())
strings = []
for i in range(0,n):
	strings.append(str(raw_input()))

q = int(raw_input())
queries = []
for j in range(0,q):
	queries.append(str(raw_input()))

for s in range(0,q):
	print (strings.count(queries[s]))
