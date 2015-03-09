import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c

file = 'OptTr-checking_learning-2choices-300ms.npy'
load = np.load(file)
Optimum_trials = np.zeros(load.shape[1])
for i in range(0,load.shape[0],1):
    Optimum_trials += load[i,:]

Optimum_trials = Optimum_trials/float(load.shape[0])
file = 'OptimumTrials-2choices-300ms.npy'
np.save(file, Optimum_trials)

trials = np.linspace(1,load.shape[1]+1,load.shape[1])
fitParams, fitCovariances = curve_fit(fitFunc, trials, Optimum_trials)
print fitParams

fig = plt.figure()
axes = fig.add_subplot(1,1,1)
axes.set_autoscale_on(False)
yticks = np.linspace(0,1,11)
axes.set_xbound(0,load.shape[1]+1)
axes.set_ybound(0,1.1)
axes.set_yticks(yticks)
axes.plot(trials, Optimum_trials)
axes.plot(trials, fitFunc(trials, fitParams[0], fitParams[1], fitParams[2]), "r", linewidth = 3)

plt.ylabel("Proportion of optimum trials")
plt.xlabel("Trial number")
fig.savefig("PropotionOfOptimumTrials-2choices-500ms.pdf")
plt.show()
