n = int(raw_input())

names = []
scores = []
for i in range(0,n):
	name = str(raw_input())
	names.append(name)
	score = float(raw_input())
	scores.append(score)

#newone = [[N,S] for N,S in zip(names,scores)]
newone = []
for N,S in zip(names,scores):
	newone.append([N,S])

uscores = list(sorted(scores))
print uscores
val = uscores[1]
print val
#ind = scores.index(val)
indices = [i for i, x in enumerate(scores) if x == val]
namesnew = []
for m in indices:
	namesnew.append(names[m])
final = sorted(namesnew)
print '\n'.join(final)

