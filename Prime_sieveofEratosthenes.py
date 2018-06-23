import math
#import sympy

def isPrime(n):
	if n<2:
		return False
	for i in range(2,int(n**0.5)+1):
		if n%i == 0:
			return False
	return True

def PrimeSieve(n):
	sieve = [True]*n
	sieve[0] = False
	sieve[1] = False

	for i in range(2,int(n**0.5)+1):
		pointer = i*2
		while pointer < n:
			sieve[pointer] = False
			pointer += 1

	primes = []
	for i in range(n):
		if sieve[i] == True:
			primes.append(i)
	return primes

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

n = int(raw_input())
result = primes2(n)
print result