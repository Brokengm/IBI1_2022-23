def determine(seq): # define the function
    seq=seq.upper() # let the seq be upper case
    start = seq.find('ATG') # get the location of start codon
    end = seq.find('TGA') # get the location of end codon
    length=len(seq[start:end+2]) # calculate the length/distance
    percent = str(length/len(seq)*100)+'%' # calculate the percent
    if length > len(seq)/2:  # judgment
        return percent+' '+'protein-coding'
    elif length < len(seq)/10:
        return percent+" "+'non-coding'
    else:
        return percent+' '+'unclear'
seq = 'ATGcTCATCACTACTATCTGA' # example
a = determine(seq)
print(a)