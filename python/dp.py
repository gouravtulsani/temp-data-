a = [2,2,0,2,1,3,3,2,1,0,2,4,3]

n = len(a)
v=[]
for i in range(n):
	v.append(False)
v[0]=True
for i in range(n):
	r = i+a[i] if (i+a[i]<n) else n-1
	
	for j in range(i+1, r+1):
		if(v[j]==False):
			v[j] = True



if all(x==v[0] for x in v):
	print True
else:
	print False


















