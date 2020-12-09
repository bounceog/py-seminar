# coding: utf8 
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('src')

from utils import *

# TODO
def process():
    res = {
        'raucher': [0, 0, 0, 0],
        'nichtraucher': [0, 0, 0, 0]
    }

    smokers_num = values_alloc(data, 'raucher')
    bp_sys_smoker_alloc = spec_key_alloc(data, 'messwert_bp_sys', 'raucher', True)
    bp_sys_nonsmoker_alloc = spec_key_alloc(data, 'messwert_bp_sys', 'raucher', False)

    for key in bp_sys_smoker_alloc:
        if key in range(0, 104):
            res['raucher'][0] += bp_sys_smoker_alloc[key]
        elif key in range(105, 119):
            res['raucher'][1] += bp_sys_smoker_alloc[key]
        elif key in range(120, 129):
            res['raucher'][2] += bp_sys_smoker_alloc[key]
        elif key in range(130, 200):
            res['raucher'][3] += bp_sys_smoker_alloc[key]
    
    for key in bp_sys_nonsmoker_alloc:
        if key in range(0, 105):
            res['nichtraucher'][0] += bp_sys_nonsmoker_alloc[key]
        elif key in range(105, 120):
            res['nichtraucher'][1] += bp_sys_nonsmoker_alloc[key]
        elif key in range(120, 130):
            res['nichtraucher'][2] += bp_sys_nonsmoker_alloc[key]
        elif key in range(130, 200):
            res['nichtraucher'][3] += bp_sys_nonsmoker_alloc[key]

    for key in res: 
        for i in range(len(res[key])):
            if key == 'raucher':
                res[key][i] = round(res[key][i] / smokers_num[True] * 100, 2)
            else:
                res[key][i] = round(res[key][i] / smokers_num[False] * 100, 2)

    return res


def show():
    labels = ['Niedrig', 'Optimal', 'Normal', 'Hochnormal']

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, proc_data['raucher'], width, label='Raucher')
    rects2 = ax.bar(x + width/2, proc_data['nichtraucher'], width, label='Nichtraucher')

    ax.set_ylabel('Anzahl Patienten')
    ax.set_title('Bluthochdruckverteilung von Rauchern und Nichtrauchern in %')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    data = load_data()
    proc_data = process()

    show()