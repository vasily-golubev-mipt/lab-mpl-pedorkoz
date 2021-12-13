import numpy as np
import matplotlib.pyplot as plt

with open('frames.dat', 'r', encoding="utf-8") as f:
    d = f.read().split('\n')
for i in range(len(d)):
    d[i] = d[i].split(' ')

x = []
y = []

for i in range(len(d) - 1):
    for j in range(len(d[i])):
        if i % 2 == 0:
            x.append(np.double(d[i][j]))
        else:
            y.append(np.double(d[i][j]))
    if i % 2 == 1:
        print(len(x), len(y))
        n = i // 2 + 1
        plt.subplot(2, 3, n)
        plt.plot(x, y)
        plt.grid()
        plt.title('Frame'+ str(n))
        plt.xticks(np.arange(0, 16, 2))
        plt.yticks(np.arange(-10, 14, 2))
        x = []
        y = []
plt.tight_layout()
plt.show()
plt.savefig('frames.png')

