n=int(input())
dom = [int(i) for i in input().split()]
brian=[int(i) for i in input().split()]
ddom = []
dbrain = []
for i in range(0,n-1):
	ddom.append(abs(dom[i]-dom[i+1]))
	dbrain.append(abs(brian[i]-brian[i+1]))

if (max(dbrain)) > (max(ddom)):
	print("Brain")
	print(max(dbrain))
elif (max(dbrain)) < (max(ddom)):
	print("Dom")
	print(max(ddom))
else:
	print("Tie")