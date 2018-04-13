l=[x for x in input().split('"')]
l1=[x for x in l if len(x)>2]
print(l1)
d=[[x for x in range(0,9)]for y in range(0,9)]
for i in range(0,9):
	for j in range(0,9):
		if(l1[i][j]=='.'):
			d[i][j]=0
		else:
			d[i][j]=int(l1[i][j])
for i in range(0,9):
	print(d[i])

def check(a):
	f=1
	count=[0 for j in range(0,9)]	
	for i in range(0,9):
		if(a[i]!=0):
			count[a[i]-1]+=1
	#print(count)
	for i in range(0,9):
		if(count[i]>1):
			f=0
			break
	return f
p=0
for i in range(0,27):	
	a=[0 for x in range(0,9)]	
	if(i<9):
		a=d[i][:]
	#	print(a)
	elif(i>8 and i<18):
		for j in range(0,9):		
			a[j]=d[j][i-9]
	#	print(a)
	else:
		if(i>17 and i<21):
			for k in range(0,9):
				if(k<3):
					a[k]=d[i-(18-p)][k]
				elif(k>2 and k<6):
					a[k]=d[i-(17-p)][k-3]
				else:
					a[k]=d[i-(16-p)][k-6]
			p+=2
		if(i>20 and i<24):
			#print(p)			
			for k in range(0,9):
				if(k<3):
					a[k]=d[i-(15+p)][k+3]
				elif(k>2 and k<6):
					a[k]=d[i-(14+p)][k]
				else:
					a[k]=d[i-(13+p)][k-3]
			p-=2
		elif(i>23 and i<27):
			#print(p)
			for k in range(0,9):
				if(k<3):
					a[k]=d[i-(24-p)][k+6]
				elif(k>2 and k<6):
					a[k]=d[i-(23-p)][k+3]
				else:
					a[k]=d[i-(22-p)][k]
			p+=2
	#print(a)
	f=check(a)
	#print(f)
	if(f==0):
		break
if(f==0):
	print(0)
else:
	print(1)



