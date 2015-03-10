import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c

file = 'Weights-2choices-300ms.npy'
load = np.load(file)

fig = plt.figure()
axes = fig.add_subplot(1,1,1)
plt.boxplot([load[:,0], load[:,1], load[:,2], load[:,3]])
plt.ylabel("Weights")
plt.xticks([1, 2, 3, 4], ["1", "2","3", "4"])
plt.ylim(0.4,0.8)

fig.savefig("Weights-2choices-300ms.pdf")
plt.show()
