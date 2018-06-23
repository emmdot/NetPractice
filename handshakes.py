import math

n = int(raw_input())
for i in range(n):
	people = int(raw_input())
	handshakes = (people*(people - 1))/2
	print handshakes