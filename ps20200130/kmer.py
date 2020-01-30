n=input('정수를 입력하세요: ')
n=int(n)

origin=['A','T','G','C']
answer=['A','T','G','C']

for i in range(n-1):
	temp=[]
	for i in origin:
		for j in answer:
			temp.append(i+j)
	answer=temp

print(answer)
print(len(answer))