#help from zhihu, URL:https://www.zhihu.com/tardis/zm/art/30024792?source_id=1005
class triathlon(object): # define a class
    def __init__(self,name,location,swim,cycle,run,total_time): #define the parameter of instance in class
        self.name=name
        self.location=location
        self.swim= swim
        self.cycle=cycle
        self.run=run
        self.total_time=total_time
name="Adam_Marion" # example
location = "Haining"
swim = "7" # use minute as default unit
cycle = '7'
run = "1"
total_time = str(int(cycle) + int(swim) + int(run))+'min'
triathlon1 = triathlon(name,location,swim,cycle,run,total_time) # create an instance
print(triathlon1.name,triathlon1.location,triathlon1.swim+'min',triathlon1.cycle+'min',triathlon1.run+'min',triathlon1.total_time)