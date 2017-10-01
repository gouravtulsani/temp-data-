b=10
def add(a):
	if a<1:
		pass
	else:
		print b-(a-1)
		a -= 1
		return add(a)
		

add(10)