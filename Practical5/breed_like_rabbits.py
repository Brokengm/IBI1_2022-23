#While sum <= 100 
# run
#sum=2*sum generation= generation + 1
#sum originally = 2 generation originally =1
sum = 2
generation = 1
n = 0 #newborn each generation
while sum <= 100:
        n=sum
        sum=2*sum
        print (n,"rabbits are born in" ,generation, "generation")
        generation=generation + 1
print (generation, "generations are needed")
