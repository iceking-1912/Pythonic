
# ------------------------------------------------------------
# *Learn MatPlotLib Here

#* All Imports

from matplotlib import pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.xkcd()

# *Data sets 
xaxis = [20, 21, 22, 23, 24, 25, 26]
demand =(816, 830, 850, 900, 950, 968, 1000)
yaxis = [500, 560, 570, 580, 650, 675, 700]

# *Lets plot

p
lt.plot(xaxis, yaxis,color='#',marker='.',label='- Salary')
plt.plot(xaxis, demand,LineStyle='--',marker='o',label='-Demand')

# *Labels

plt.xlabel('Age')
plt.ylabel('Salary and Demand')

# *Titles
plt.title("") 

# * Legends
plt.legend()

# *Lets Look The Plot


plt.tight_layout()
plt.grid(True)

plt.show()

plt.savefig('comic_plot.png')
