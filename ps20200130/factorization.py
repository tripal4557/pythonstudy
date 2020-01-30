def a(n):
	divider=2
	factors={}
	while True:
		if n%divider==0:
			n=n/divider
			if not divider in factors.keys():
				factors[divider]=1
			else:
				factors[divider]+=1
		else:
			divider+=1
		if n==1:
			break
	for i in factors.keys():
		print(str(i)+' × '+str(factors[i]))

while(True):
	number=input('인수분해할 정수를 입력하세요: ')
	if number=='0':
		print('종료합니다')
		#탈출코드
		quit()
	try:
		number=int(number)
	except:
		print('정수가 아닙니다.')
		continue
	if number<=1:
		print('2 이상이어야 합니다.')
		continue
	a(number)