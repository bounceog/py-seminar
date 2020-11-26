import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('src')
from utils import *


def process():
    # TODO
    # ggf. Verarbeitung der Daten zur Darstellung
    print()


def show():
    # TODO
    # Passende Darstellung waehlen
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')

    plt.show()


if __name__ == "__main__":
    global data
    data = load_data()
    for line in data:
        print(line['terminal'])
    
    # process()
    # show()
