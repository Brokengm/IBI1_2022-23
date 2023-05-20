# help from IBI Practical 11
import blosum as bl  # import blosum matrix 62
matrix = bl.BLOSUM(62)
def read(file): #define a function to read file
    a=open(file,'r')
    b=a.read()
    c=b.split('\n')
    return c
cat=read('ACE2_cat.fa')
human=read('ACE2_human.fa')
mouse=read('ACE2_mouse.fa')
def align(file1,file2): #define a function for alignment
    sum_score=0 #define the variable of the sum of scores
    sum=0 # define the variable of the sum of similarity
    for i in range(len(file1[1])):
        sum_score +=matrix[file1[1][i]][file2[1][i]] # add the score of each comparison
        if file1[1][i]==file2[1][i]:
            sum+=1 # add each similarity
    #return the result
    return file1[0]+'\n'+file1[1]+'\n'+file2[0]+'\n'+file2[1]+'\n'+str(sum_score)+' percent='+str(sum*100/len(file1[1]))+'%'
print(align(cat,human)+'\n')
print(align(mouse,human)+'\n')
print(align(cat,mouse)+'\n')
# human ACE2 gene is more like that of cats
# The similarity between human and cat ACE2 could point to the two species sharing an ancient common ancestor, from which the gene was inherited.