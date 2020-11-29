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
data_rauch = values_alloc(raucher,'blutzucker_bekannt')
data_normal = values_alloc(data,'blutzucker_bekannt')

raucher = float(data_rauch[True])

alle = float(data_rauch[True] + data_rauch[False])


zahl = raucher/alle

print(zahl)
print(raucher / alle)
print(type(raucher))
print(type(alle))


#print(data_rauch[True])
#print((data_rauch[True] + data_rauch[False]))
# print(value_alloc(raucher,'blutzucker_bekannt'))



# plt.xlabel('Eingangszahlahl')
# plt.ylabel('Ausgangszahl')
# plt.title('Qudratzahlen bis 5')


# # plt.grid(True)
# plt.show()
