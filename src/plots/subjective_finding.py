# coding: utf8 
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('src')

from utils import *

# TODO
def process():
    print()


def show():
    x1 = np.linspace(0.0, 5.0)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)

    plt.subplots()
    plt.plot(x1, y1, 'o-')

    plt.title('Subjektives Befinden bei Rauchern')
    plt.ylabel('Bewertungsskala')

    plt.show()


if __name__ == "__main__":
    data = load_data()
    # proc_data = process()

    show()