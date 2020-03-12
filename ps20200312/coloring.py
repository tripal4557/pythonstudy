from PIL import Image, ImageDraw
import sys

input_path=sys.argv[1]
output_path=sys.argv[2]

f=open(input_path)
f.readline()
seq=f.readline()
f.close()
max=len(seq)

def allfind(seq, endcodon):
	output=[]
	i=0
	while True:
		i=seq.find(endcodon,i+1)
		if i==-1:
			break
		output.append(i)
	return output

all_end_position=allfind(seq,'TAA')+allfind(seq,'TAG')+allfind(seq,'TGA')
'''
print(all_end_position[:100])
print(len(all_end_position))
'''
#padding 20px
im=Image.new('RGB',(1040,60),(255,255,255))
draw=ImageDraw.Draw(im)
draw.rectangle((20,20,1020,40),fill='white',outline='black')

for i in all_end_position[::10]:
	x=int(1000*i/max)+20
	draw.line((x,20,x,40),fill='red',width=1)
draw.text((1000,40),str(max),'black')
im.save(output_path)