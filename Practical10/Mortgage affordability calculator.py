# help from IBI lecture 10.1
def calculator(value,salary): # define the function
    if value > salary*5:#judge
        return "No" # return the result
    else:
        return 'Yes'# return the result
value=50000 #input example
salary=20000
x=calculator(value,salary)
print(x) # print result
