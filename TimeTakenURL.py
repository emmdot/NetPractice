import time
import requests
import os
import socket

def giveRTT(url):
	t1 = time.time()
	openit = requests.get(url)
	t2 = time.time()
	taken = t2 - t1
	print "time taken in seconds: " + str(taken)


#inputurl = str(raw_input("Enter the url : \n"))
demourl = "https://www.google.com"
giveRTT(demourl)

print(os)
