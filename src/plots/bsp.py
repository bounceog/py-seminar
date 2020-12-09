# coding: utf8 
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('src')

from utils import *


def process():
    # TODO
    print('')

def show():
    x_indizes = np.arange(-5,6)

    y_werte = [25,16,9,4,1,0,1,4,9,16,20]
    y_werte = np.power(x_indizes,3)

    fig, ax = plt.subplots()

    line1, = ax.plot(x_indizes, y_werte, linestyle='dashed', label="Line 1")
    line2, = ax.plot(x_indizes, y_werte + 10, linestyle='-.', label="Line 2")

    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    plt.xticks(x_indizes, labels)

    ax.set_xlabel('x-label', fontsize=18)
    ax.set_ylabel('y-label', fontsize=18)

    ax.set_title('Title', fontsize=24)

    ax.legend()

    plt.show()



if __name__ == "__main__":
    data = load_data()
    # proc_data = process()

    show()