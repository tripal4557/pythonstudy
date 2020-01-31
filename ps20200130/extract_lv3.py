#SNP와 GENE의 모든 라인을 배열로 저장한 뒤 일일히 대조
import csv

f=open('snp_info.csv')
rd=csv.reader(f)
snp=list(rd)
f.close()

g=open('gene_info_lv3.csv')
rd=csv.reader(g)
gene=list(rd)
g.close()

del snp[0]
del gene[0]

#SNP:[0] id, [1] Position
#GENE: [0]id, [1] start, [2] end, [3] direction
#글자를 숫자로 바꿔주도록 한다

for i in snp:
	i[1]=int(i[1])

for j in gene:
	j[1]=int(j[1])
	j[2]=int(j[2])

h=open('extract_lv3.csv','w',newline='')
wr=csv.writer(h)

for i in snp:
	for j in gene:
		if int(j[1])<=int(i[1])<=j[2]:
			stream='exon'
		elif j[2]<i[1]<=j[2]+500:
			if j[3]=='+':
				stream='downstream'
			else:
				stream='upstream'
		elif j[1]-500<=i[1]<j[1]:
			if j[3]=='+':
				stream='upstream'
			else:
				stream='downstream'
		else:
			continue
		wr.writerow(i+j+[stream])

h.close()
print('end')