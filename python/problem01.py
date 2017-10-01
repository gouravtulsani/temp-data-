a= [[2,3],[3,2],[5,6],[6,7],[2,4],[10,15]]
lis = []
for i in range(0,len(a)-1):
	for j in range(0,len(a[i])):
		if a[i][j] == a[i+1][0] or a[i][j] == a[i+1][1]:
			lis.append(a[i][j])

print lis
	