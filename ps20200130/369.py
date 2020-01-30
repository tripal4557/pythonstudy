a=list(range(1,101))
print('a created')
print(a[:10])

b=[]
for i in a:
	b.append(str(i))
print('b created')
print(b[:10])

c=[]
for i in b:
	if '3' in i or '6' in i or '9' in i:
		c.append(i)
print('c created')
print(c)