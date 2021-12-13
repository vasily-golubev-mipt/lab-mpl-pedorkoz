import numpy as np
import matplotlib.pyplot as plt

try:
    with open('005.dat', 'r', encoding="utf-8") as f:
        d = f.read().split('\n')
    for i in range(1, len(d)):
        d[i] = d[i].split(' ')
    x = []
    y = []
    for i in range(1, int(d[0]) + 1):
        x.append(float(d[i][0]))
        y.append(float(d[i][1]))
    plt.scatter(x, y)
    plt.axis('equal')
    plt.axis('scaled')
    plt.axis([min(x) - 10, max(x) + 10, min(y) - 10, max(y) + 10])

    plt.title(f'Number of points: {d[0]}')
    plt.show()
    plt.savefig('005.png')

except:
    pass





#