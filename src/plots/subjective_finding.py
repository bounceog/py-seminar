# coding: utf8 
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

sys.path.append('src')

from utils import *


def process():
    sub_finding = spec_key_alloc(data, 'befinden', 'raucher', True)

    res = {
        'x': [],
        'y': []
    }

    for key in sub_finding:
        res['x'].append(int(key))
        res['y'].append(sub_finding[key])
    
    return res


def show():
    plt.subplots()
    plt.plot(np.sort(proc_data['x']), np.array(proc_data['y']), 'o--')

    plt.title('Subjektives Befinden bei Rauchern')
    plt.ylabel('Anzahl Stimmen')
    plt.xlabel('Bewertungsskala')

    plt.show()


if __name__ == "__main__":
    data = load_data()
    proc_data = process()

    show()