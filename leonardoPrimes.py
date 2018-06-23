
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
accumulated_array = [2]
for i in range(0,14):
	accumulated_array.append(accumulated_array[i]*primes[i+1])

n = int(raw_input())
for j in range(0,n):
	que = int(raw_input())
	if que > 1:
		count = 0
		for iterator in range(0,15):
			if que > accumulated_array[iterator]:
				count += 1
			else:
				break
		print count
	else:
		print 0


