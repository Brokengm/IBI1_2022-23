costs=[1,8,15,7,5,14,43,40]
#sort the list
costs=sorted(costs)
import matplotlib.pyplot as plt
#value x y axis
y=costs
x=['Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2003','Beijing 2008','London 2012']
#set the size of figure
plt.figure(figsize = (9, 3))
plt.bar(x,y)
#make labels smaller and rotate them
plt.xticks(fontsize = 6, rotation= 45)
plt.show()
