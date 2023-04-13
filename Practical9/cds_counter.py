#we first find the number of start codon and stop codon,
# the calculate the the number of combination of start codon and stop codon
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
a=seq.count('ATG') #the number of start codon
b=seq.count('TGA')#the number of stop codon
c=seq.count('TAA')
wholenum=a*b+a*c# the number of sequence possible
print(wholenum)