import numpy as np
import matplotlib.pyplot as plt
def plotfunc(no_groups,group1,group2,label):
    
    no_groups = 9
    index = np.arange(no_groups)
    bar_width = 0.4
    opacity = 0.8

    plt.bar(index, group1, bar_width,
    alpha=opacity,
    color='b',
    label='benford')

    plt.bar(index + bar_width, group2, bar_width,
    alpha=opacity,
    color='g',
    label=label)

    plt.xlabel('digit')
    plt.ylabel('percentage')
    plt.title('bar chart')
    plt.xticks(index + bar_width, ('1', '2', '3', '4' , '5' , '6' , '7' , '8' , '9'))
    plt.legend()

    plt.tight_layout()
    plt.show()
