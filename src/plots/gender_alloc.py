# coding: utf8 
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('src')

from utils import *


def process():
    gender_alloc = value_alloc(data, 'geschlecht')
    data_size = get_data_size(data)

    result = []

    for key in gender_alloc:
        result.append(gender_alloc[key] / data_size * 100)

    return result


def show():
    labels = 'Männer', 'Frauen'
    explode = (0.1, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(proc_data, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()


if __name__ == "__main__":
    data = load_data()
    proc_data = process()

    show()

