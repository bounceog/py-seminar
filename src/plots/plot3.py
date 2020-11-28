import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('src')
from utils import *


        
# print('hello world')

# plt.style.use('fivethirtyeight')

# plt.legend()
data = load_data()

raucher = get_boolitems(data,'raucher')
data_rauch = value_alloc(raucher,'blutzucker_bekannt')
data_normal = value_alloc(data,'blutzucker_bekannt')

# a = str((data_rauch[True]/(data_rauch[True]+data_rauch[False]))*100)
print(data_rauch[True])
print((data_rauch[True]+data_rauch[False]))
# print(value_alloc(raucher,'blutzucker_bekannt'))



# plt.xlabel('Eingangszahlahl')
# plt.ylabel('Ausgangszahl')
# plt.title('Qudratzahlen bis 5')


# # plt.grid(True)
# plt.show()
