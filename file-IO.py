import sys
import os
import pickle

text = 'Bazoomba'
with open('demo.txt','wt') as f:
	f.write(text)

f1 = open('demo.txt','rt')
for line in f1:
	print line


#sys.stdout.buffer.write(b'hello\n')

data = 'this is a test for pickle.Nevermind'
fd = open('newfile.pkl','wb')
pickle.dump(data,fd)

