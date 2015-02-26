import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia_Model/')
import parameters_Nico as p

def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c
print p.rt
file = p.rt + '/LearningOptimumTrials.npy'
load = np.load(file)

Optimum_trials = np.zeros(load.shape[1])
for i in range(0,load.shape[0],1):
    Optimum_trials += load[i,:]

Optimum_trials = Optimum_trials/float(load.shape[0])
file = p.rt + '/OptimumTrials.npy'
np.save(file, Optimum_trials)

trials = np.linspace(1,load.shape[1]+1,load.shape[1])
fitParams, fitCovariances = curve_fit(fitFunc, trials, Optimum_trials)

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
file = p.rt + "/LearningCurve.png"
fig.savefig(file)
plt.show()
