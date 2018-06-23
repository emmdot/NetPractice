def summingSeries(n):
	summ = 0
	for i in range(1,n+1):
		summ = summ + (2*i - 1)
	return summ
 
 
t = int(raw_input())
for _ in range(t):
	n = int(raw_input())
	res = summingSeries(n)
	print res