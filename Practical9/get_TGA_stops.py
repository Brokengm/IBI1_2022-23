#Help from IBI1 lecture9 and classmates
import os
os.chdir('C:/Users/dyq37') #change working directory
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')#open file
a=xfile.read()#read file
b=a.split('>')#split the text into separate parts
newfile=open('TGA_genes.fa','w')#create a new file
for i in b:
    if i.endswith('TGA\n'): #find the correct line
        c=i.find('ATG')#get start codon
        d=i.split()#get the name
        newfile.write(d[0]+'\n')#add name
        newfile.write(i[c:])#add sequence
    else:
        continue