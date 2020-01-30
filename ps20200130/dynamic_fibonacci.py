n=input('정수를 입력하세요: ')
n=int(n)
answer=[1,1]

#classic

for i in range(n-2):
	answer.append(answer[-1]+answer[-2])
print(answer)