import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')

from parameters import *

protocol = input('Choose 1 for Guthrie-Protocol or 2 for Piron-Protocol\n')
if protocol == 1:
	inverse = input('\nDo you want to have an inverse of Probabilities during the simulation?\nChoose 1 for True or 0 for False\n')
	folder = 'Results'
	title = 'Normal Probabilities'
	if inverse:
		inverse_trial = input('\nAfter how many trials will be the inverse?\n')
		inverse_all = input('\nDo you want to inverse all probabilities or just the middle ones?\nChoose 1 for all or 0 for middle ones\n')
		folder += '-inverse-after' + str(inverse_trial)
		folder += 'all' if inverse_all else 'middle cues'#-NoCortLearn-HalfParam
		title = 'Inverse probabilities of '
		title += 'all ' if inverse_all else 'middle cues '
		title += 'cues after %s trials\nWeights from ' %str(inverse_trial)


elif protocol == 2:
	folder = '../cython/Piron-Protocol/Results-HalfParam'

file = folder + '/Weights_Cog.npy'
load = np.load(file)
MeanWeights = load.mean(axis = 0)
t = np.arange(MeanWeights[:,0].shape[0])
StdWeights = load.std(axis = 0)
#MeanWeights = (MeanWeights - np.min(MeanWeights)) / (np.max(MeanWeights) - np.min(MeanWeights))
file = folder+ '/MeanWeights-Cog.npy'
np.save(file, MeanWeights)

fig, ax = plt.subplots(1)
ax.plot(MeanWeights[:,0], c = 'b', label = '1st cue')
ax.fill_between(t, MeanWeights[:,0]-StdWeights[:,0], MeanWeights[:,0]+StdWeights[:,0], facecolor='grey')
plt.plot(MeanWeights[:,1], c = 'r', label = '2nd cue')
ax.fill_between(t, MeanWeights[:,1]-StdWeights[:,1], MeanWeights[:,1]+StdWeights[:,1], facecolor='grey')
plt.plot(MeanWeights[:,2], c = 'g', label = '3rd cue')
ax.fill_between(t, MeanWeights[:,2]-StdWeights[:,2], MeanWeights[:,2]+StdWeights[:,2], facecolor='grey')
plt.plot(MeanWeights[:,3], c = 'm', label = '4th cue')
ax.fill_between(t, MeanWeights[:,3]-StdWeights[:,3], MeanWeights[:,3]+StdWeights[:,3], facecolor='grey')
plt.legend(loc='upper left')

plt.ylabel("Weights")
plt.xlabel("Trial number")
temp_title = title + 'Cognitive to Associative Cortex'
plt.title(temp_title)
plt.ylim(0.495,0.55)
file = folder + "/Weights-Cog.png"
fig.savefig(file)

file = folder + '/Weights_Mot.npy'
load = np.load(file)
MeanWeights = load.mean(axis = 0)
t = np.arange(MeanWeights[:,0].shape[0])
StdWeights = load.std(axis = 0)
#MeanWeights = (MeanWeights - np.min(MeanWeights)) / (np.max(MeanWeights) - np.min(MeanWeights))
file = folder+ '/MeanWeights-Mot.npy'
np.save(file, MeanWeights)

fig, ax = plt.subplots(1)
ax.plot(MeanWeights[:,0], c = 'b', label = '1st cue')
ax.fill_between(t, MeanWeights[:,0]-StdWeights[:,0], MeanWeights[:,0]+StdWeights[:,0], facecolor='grey')
plt.plot(MeanWeights[:,1], c = 'r', label = '2nd cue')
ax.fill_between(t, MeanWeights[:,1]-StdWeights[:,1], MeanWeights[:,1]+StdWeights[:,1], facecolor='grey')
plt.plot(MeanWeights[:,2], c = 'g', label = '3rd cue')
ax.fill_between(t, MeanWeights[:,2]-StdWeights[:,2], MeanWeights[:,2]+StdWeights[:,2], facecolor='grey')
plt.plot(MeanWeights[:,3], c = 'm', label = '4th cue')
ax.fill_between(t, MeanWeights[:,3]-StdWeights[:,3], MeanWeights[:,3]+StdWeights[:,3], facecolor='grey')
plt.legend(loc='upper left')

plt.ylabel("Weights")
plt.xlabel("Trial number")
temp_title = title + 'Motor to Associative Cortex'
plt.title(temp_title)
plt.ylim(0.495,0.52)
file = folder + "/Weights-Mot.png"
fig.savefig(file)

file = folder + '/Weights_Str.npy'
load = np.load(file)
MeanWeights = (load.mean(axis = 0) - Wmin) / (Wmax - Wmin)
t = np.arange(MeanWeights[:,0].shape[0])
StdWeights = load.std(axis = 0)
file = folder+ '/MeanWeights-Str.npy'
np.save(file, MeanWeights)

fig, ax = plt.subplots(1)
ax.plot(MeanWeights[:,0], c = 'b', label = '1st cue')
ax.fill_between(t, MeanWeights[:,0]-StdWeights[:,0], MeanWeights[:,0]+StdWeights[:,0], facecolor='grey')
plt.plot(MeanWeights[:,1], c = 'r', label = '2nd cue')
ax.fill_between(t, MeanWeights[:,1]-StdWeights[:,1], MeanWeights[:,1]+StdWeights[:,1], facecolor='grey')
plt.plot(MeanWeights[:,2], c = 'g', label = '3rd cue')
ax.fill_between(t, MeanWeights[:,2]-StdWeights[:,2], MeanWeights[:,2]+StdWeights[:,2], facecolor='grey')
plt.plot(MeanWeights[:,3], c = 'm', label = '4th cue')
ax.fill_between(t, MeanWeights[:,3]-StdWeights[:,3], MeanWeights[:,3]+StdWeights[:,3], facecolor='grey')
plt.legend(loc='upper left')

plt.ylabel("Weights")
plt.xlabel("Trial number")
temp_title = title + 'Cognitive Cortex to Cognitive Striatum'
plt.title(temp_title)
#plt.ylim(0.4,0.80)
file = folder + "/Weights-dStr.png"
fig.savefig(file)



plt.show()
