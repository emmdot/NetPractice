n = int(raw_input())

if n%2 == 0:
	if n<=5 and n>=2:
		print "Not Weird"
	if n>=6 and n<=20:
		print "Weird"
	if n>20:
		print "Not Weird"
else:
	print "Weird" 