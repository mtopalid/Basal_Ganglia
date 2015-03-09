import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2014/Guthrie-Protocol/cython/')


def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c
path = 'Results_DiffNoise_InitW_120tr_test'
file = path + '/Performance-test-NoGPi.npy'
load = np.load(file)
mean =  load.mean(axis = 0).mean()#[:,109:119]
Optimum_trials = np.zeros(load.shape[1])
for i in range(0,load.shape[0],1):
    Optimum_trials += load[i,:]

Optimum_trials = Optimum_trials/float(load.shape[0])
file = path+ '/OptimumTrials-test-NoGPi.npy'
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
plt.title('Mean Performance: ' + str(mean))#of 10 last trials
file = path + "/LearningCurve-test-NoGPi.png"
fig.savefig(file)
plt.show()
