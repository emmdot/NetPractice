import math
import numpy as np
nm = map(int,raw_input().rstrip().split())
n,m = nm[0],nm[1]

#arr = np.zeros([n,n], dtype = int)
arr =[]

for z in range(n):
	arr.append(0)
queries = []
for i in range(m):
	temp = map(int,raw_input().rstrip().split(' '))
	queries.append(temp)

for x in range(m):
	for y in range(queries[x][0],queries[x][1]):
		arr[y] += queries[x][2]

print max(arr)




