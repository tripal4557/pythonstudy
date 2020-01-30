n=input('정수를 입력하세요: ')
n=int(n)

#normal factorial
'''
answer=1
for i in range(n):
	answer=answer*(i+1)
	print(answer)
'''

#recursive factorial
def facto(n):
	if n==1:
		return 1
	else:
		print(n)
		return n*facto(n-1)
print(facto(n))