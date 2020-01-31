#SNP와 GENE의 모든 라인을 배열로 저장한 뒤 일일히 대조
import csv

f=open('snp_info.csv')
rd=csv.reader(f)
snp=list(rd)
f.close()

g=open('gene_info_lv2.csv')
rd=csv.reader(g)
gene=list(rd)
g.close()

del snp[0]
del gene[0]

h=open('extract_lv2.csv','w',newline='')
wr=csv.writer(h)

for i in snp:
	for j in gene:
		distance=int(i[1])-int(j[1])
		if abs(distance)<=500:
			if distance>=0 and j[2]=='+':
				stream='downstream'
			elif distance<0 and j[2]=='-':
				stream='downstream'
			else:
				stream='upstream'
			wr.writerow(i+j+[stream])

h.close()
print('end')