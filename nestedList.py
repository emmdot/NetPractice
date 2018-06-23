mealcost = float(raw_input())
tip = int(raw_input())
tipval = float((mealcost*tip)/100)
#print tipval
tax = int(raw_input())
taxval = float((mealcost*tax)/100)
#print taxval
total = mealcost + tipval + taxval
print "The total meal cost is " + str(int(round(total))) + " dollars."