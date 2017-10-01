#a= input()
#b=[int(i) for i in input().split(' ')]
b =[4545, 564, 464, 5464, 546, 54, 64, 646, 464, 5445, 46]
len_of_b = len(b)
for i in range(0,int(input())):
	d=int(input())
	for i in range(0, len_of_b):
		b[i]=int(int(b[i])/d)

for i in b:
	print(i, end=' ')