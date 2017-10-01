import sys
a = sys.argv
result=[]
for i in a[1]:
	if i in result:
		pass
	else:
		result.append(i)
for i in range(len(result)-1,-1,-1):
	print result[i],