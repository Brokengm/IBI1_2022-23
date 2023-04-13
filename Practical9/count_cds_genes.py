#Help from IBI1 lecture9 and classmates
import os
codon=input('end_codon=') #I find the input should be like TAA instead of 'TAA' or the file will be nothing
os.chdir('C:/Users/dyq37') #change working directory
xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')#open file
a=xfile.read()#read file
b = a.split('>')#split the text into separate parts
newfile=open(codon+'_stop_genes.fa','w')#create the file
for i in b:
    if i.endswith(codon+'\n'): #find the correct line
        c=i.find('ATG')#get the start codon
        d=i.split()#get the name
        e=i.count(codon)#get the number of coding sequence
        newfile.write(d[0]+'\000'+str(e)+'\n')#add name
        newfile.write(i[c:])#add sequence
    else:
        continue