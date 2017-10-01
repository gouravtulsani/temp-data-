time = '12:45:54PM'

a = list(time.split(":"))
a[2]=a[2][:2]

if time.find('PM')==8:
	a[0] = int(a[0])+12
if a[0] == "12" and time.find('PM')==8:
	a[0] = "00"
if a[0] == "12" and time.find('AM')==8:
	a[0] = "00"



print(str(a[0])+':'+a[1]+':'+a[2])