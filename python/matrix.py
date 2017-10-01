'''for i in range(int(input())):
	m, n, k = map(int, input().split())
	a = list(map(int, input().split(' ')))
	

print(a)'''


a= [[1,2],[5,4]]
def swap(a,b):
	a = a+b
	b = a-b
	a = a-b
	return a,b

for i in range(len(a)):
	for j in range(len(a)):
		swap(a[i][j],a[j][i])


for i in a:
	print(i)


