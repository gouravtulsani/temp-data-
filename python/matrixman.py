mat = [[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,1,1,0,1]]
m,n=4,4
for i in range(5):
	for j in range(5):
		if mat[i][j]==0:
			mat[i][j]='-'

def function(mat,x,y):
	if x < 0 or x >= 5 or y < 0 or y >= 5:
		return
	elif mat[x][y] != '-':
		return
	
	mat[x][y]='0'


	function(mat, x+1, y)
	function(mat, x-1, y)
	function(mat, x, y+1)
	function(mat, x, y-1)




for i in range(5):
	if mat[i][0] == '-':
		function(mat,i,0)

for i in range(5):
	if mat[i][4] == '-':
		function(mat,i,4)

for i in range(5):
	if mat[0][i] == '-':
		function(mat,0,i)

for i in range(5):
	if mat[4][i] == '-':
		function(mat,4,i)


for i in range(5):
	for j in range(5):
		if mat[i][j] == '-':
			mat[i][j] = 1


for i in mat: 
	print 