import matplotlib.pyplot as plt
import numpy as np


x_indizes = np.arange(-5,6)

y_werte = [25,16,9,4,1,0,1,4,9,16,20]


y_werte = np.power(x_indizes,3)

print()
print(y_werte)
print()

plt.plot(x_indizes, y_werte)


plt.show()

# y = np.square(x_ndarray)

# plt.plot(x_ndarray, y)

# plt.show()
