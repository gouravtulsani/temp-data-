string = '574674546476'
string = string[::-1]
count=0
result=[]
i=len(string)
while i > 0:
	for j in range(0,i):
		if int(string[j])%2==0:
			count +=1
	result.append(count)
	i-=1
	count=0
for i in result:
	print(i, end=' ')
print('')