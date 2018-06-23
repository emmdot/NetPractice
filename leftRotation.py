import sys

thend = map(int,raw_input().split())
n = thend[0]
d = thend[1]

r = d%n

arr = map(int, raw_input().rstrip().split())
'''
def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)
'''

new = arr[r:] + arr[:r]

for w in xrange(len(arr)):
	print new[w],



