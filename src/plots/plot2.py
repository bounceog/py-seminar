import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('src')
from utils import *

# print('hello world')

# plt.style.use('fivethirtyeight')

width= 0.5

zahlen_x = [1,2,3,4,5]

quad_y = [1,4,9,16,25]
cube_y = [1,8,27,64,125]

x_index = np.arange(len(zahlen_x))

# fmt_q = ':k'
# fmt_c = 'c'

plt.bar(x_index - width,quad_y,width=width, label='Qudratzahlen', color='c')
plt.bar(x_index,cube_y,width=width, label='Kubikzahlen', color='k')

plt.legend()

plt.grid(True)

plt.xlabel('Eingangszahlahl')
plt.ylabel('Ausgangszahl')
plt.title('Qudratzahlen bis 5')


plt.show()
