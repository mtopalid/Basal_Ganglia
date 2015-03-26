import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython')

from parameters import *

def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c

folder = '../cython/Guthrie/Results+test'#-HalfParam
file = folder + '/RT.npy'
load = np.load(file)
MeanRT = load.mean(axis = 0)
file = folder + '/RT-test-bg.npy'
load = np.load(file)
MeanRTtestBG = load.mean(axis = 0)
file = folder + '/RT-test.npy'
load = np.load(file)
MeanRTtest = load.mean(axis = 0)
file = folder + '/RT-test-ctx.npy'
load = np.load(file)
MeanRTtestCTX = load.mean(axis = 0)

#file = folder+ '/MeanPerformance.npy'
#np.save(file, MeanPerformance)

fig = plt.figure()
plt.plot(MeanRT, c = 'b', label = 'RT')
plt.plot(MeanRTtest, c = 'r', label = 'No GPi --> Thalamus connection')
plt.plot(MeanRTtestBG, c = 'g', label = 'No cortical learning')
plt.plot(MeanRTtestCTX, c = 'm', label = 'No striatal learning')
plt.legend()

plt.ylabel("Response Time (ms)")
plt.xlabel("Trial number")
plt.title("Topalidou model")
#plt.ylim(0.495,0.51)
file = folder + "/RT-BG-vs-Ctx.png"
fig.savefig(file)

fig = plt.figure()
plt.plot(abs(MeanRTtestBG-MeanRT), c = 'b', label = 'RT diff')
plt.title('No cortical learning: MeanRTtestBG-MeanRT')
plt.show()
fig = plt.figure()
plt.plot(abs(MeanRTtestBG-MeanRTtestCTX), c = 'b', label = 'RT diff')
plt.title('No cortical learning VS No striatal learning')
plt.show()
fig = plt.figure()
plt.plot(abs(MeanRTtestCTX-MeanRT), c = 'b', label = 'RT diff')
plt.title('No striatal learning: MeanRTtestCTX-MeanRT')
plt.show()
