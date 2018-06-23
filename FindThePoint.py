import math

n = int(raw_input())

for i in range(n):
	px,py,qx,qy = map(int,raw_input().rstrip().split(' '))
	print ("{0} {1}".format(2*qx-px, 2*qy-py))