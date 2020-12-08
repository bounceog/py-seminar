import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('src')
from utils import *


        
# print('hello world')

plt.style.use('fivethirtyeight')

# plt.legend()
# data = load_data()

data = pd.read_csv('data.csv', sep=';')
# print(data)

indexNames = data[ data['geburtsjahr'] < 1920 ].index
data.drop(indexNames, inplace = True)
indexNames = data[ data['geburtsjahr'] > 1991 ].index
data.drop(indexNames, inplace = True)

# print(data)
# print(data2)
grouped_data = data.groupby('geburtsjahr')

index = np.arange(20,86,1)

keys = grouped_data.groups.keys()
list_keys = list(keys)
print(type(list_keys))
# for key in keys:
#     print(key)

values1 = grouped_data['messwert_bp_sys'].mean().values
values2 = grouped_data['messwert_bp_dia'].mean().values

# for key in values:
#     print(key)
a = []
for key in list_keys:
    a.append(2006-key)
print(a)

plt.plot(a,values1,label='Systolisch', color='k')
plt.plot(a,values2,label='Diastolisch', color='r')

plt.legend()

plt.grid(True)

plt.xlabel('Geburtsjahr')
plt.ylabel('Durchschnitt')
plt.title('Alter - Blutdruck')

# ax = plt.gca()
# ax.invert_xaxis()
plt.show()
