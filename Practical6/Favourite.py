result = { 'Comedy': 73, 'Action':42, 'Romance':38,'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}
results=[73,42,38,28,22,19,18,12,8,7]
import matplotlib.pyplot as plt
plt.pie(results)
plt.show()
a=input('input=')
print(result[a])
