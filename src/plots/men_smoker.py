# coding: utf8 
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('src')

from utils import *


def process():
    smoker_alloc = spec_key_alloc(data, 'geschlecht', 'raucher', True)
    data_size = get_data_size(data)

    result = []

    for key in smoker_alloc:
        result.append(smoker_alloc[key] / data_size * 100)

    return result


def show():
    labels = 'Raucher', 'Nichtraucher'
    explode = (0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(proc_data, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.title('Männer')
    plt.show()


if __name__ == "__main__":
    data = load_data()
    proc_data = process()

    show()

