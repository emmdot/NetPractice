def isPowerTwo(n):
	if (n==0):
		return False
	while (n != 1):
		if (n%2 != 0):
			return False
		n = n//2
	return True

def powtwo(n):
	if (n != 0) and (n&(n-1) == 0)