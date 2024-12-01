import merennetwister as mt
import linearcongruential as lc
import midsqure as ms
import matplotlib.pyplot as plt


samples = lc.random_list(1,100,10000)

print(samples)  
plt.hist(samples, bins=100000, edgecolor='black')
plt.show()
