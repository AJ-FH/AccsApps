import numpy as np
import matplotlib.pyplot as plt

file = np.genfromtxt('2016-07-11_ipm_data.txt')

plt.plot(file)
plt.grid(color='black')
y = max(file)
x = np.where(file == y)
plt.plot(x,y, 'rx')
plt.savefig('fig', dpi=300)
