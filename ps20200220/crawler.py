import requests
from bs4 import BeautifulSoup

f=open('temp_input.csv')
num=f.readline()[0:-1].split(',')
f.close()

g=open('temp_output.txt','w')
for num_sel in num:
	res=requests.get('http://ginsengdb.snu.ac.kr/annotsearch_2.php?id='+num_sel)
	#http://ginsengdb.snu.ac.kr/annotsearch_2.php?id=Pg_S8436.1
	soup=BeautifulSoup(res.content, 'html.parser')

	a=soup.find_all('td')
	b=[x.get_text() for x in a]
	g.write('\t'.join(b[b.index('Database'):])+'\n')
	print(num_sel+'done')
g.close()