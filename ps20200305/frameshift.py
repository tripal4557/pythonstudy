f=open('input.txt')
f.readline()
original=f.readline()
f.close()

#ERROR OCCURS IF LAST LETTER IS ENTER
if original[-1]=='\n':
	print('last letter error')
	quit()

max=len(original)
print('len : '+str(max))
basenum={'A':1,'T':4,'G':2,'C':3,'N':5}

a=[]
for i in original:
	a.append(basenum[i])
print('a created')
b=[5-x for x in a[::-1]]
print('b created')#REVERSE COMPLEMENT

range_start=int(input('range_start : '))
range_end=int(input('range_end : '))

g=open('output.csv','w')
for shift in range(range_start,range_end):
	count=0
	for i in range(max-shift):
		if a[i+shift]==b[i]:
			count+=1
	g.write(str(shift)+','+str(count)+'\n')
	if shift%100==0:
		print(str(shift)+' complete')
g.close()
print('end')
