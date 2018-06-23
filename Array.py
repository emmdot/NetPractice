n = int(raw_input())
theinput = list(map(int,raw_input().strip().split(' ')))
theinput.reverse()
grim = list(str(theinput))
for x in theinput:
	print x,