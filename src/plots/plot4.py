import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('src')

from utils import *


        


data = load_data()


a = []
for index in data:
    a.append(index[])



a = data['schaetzwert_bp_sys']-data['messwert_bp_sys']
# print(a)

for index in a:


        
# print(a)


# index = np.arange(20,86,1)

# keys = grouped_data.groups.keys()
# list_keys = list(keys)
# print(type(list_keys))


# values1 = grouped_data['messwert_bp_sys'].mean().values
# values2 = grouped_data['messwert_bp_dia'].mean().values


# a = []
# for key in list_keys:
#     a.append(2006-key)
# print(a)

# plt.plot(a,values1,label='Systolisch', color='k')
# plt.plot(a,values2,label='Diastolisch', color='r')

# plt.legend()

# plt.grid(True)

# plt.xlabel('Geburtsjahr')
# plt.ylabel('Durchschnitt')
# plt.title('Alter - Blutdruck')


# plt.show()
