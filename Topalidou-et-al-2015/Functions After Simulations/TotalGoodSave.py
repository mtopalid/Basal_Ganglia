import numpy as np
import os
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015')
from parameters import *

protocol = input('Choose 1 for Guthrie-Protocol or 2 for Piron-Protocol')
if protocol == 1:
	folder = '../Guthrie-Protocol/Results'
elif protocol == 2:
	folder = '../Piron-Protocol/Results'

TotalGood = folder + '/TotalGood-withoutBad.txt'#.txt'
f = open(TotalGood, 'wb')

file = folder + '/total_good_Fam_GPi.npy'
load = np.load(file)
#print load
where = np.asarray(np.where(load>90)[0])
bad = np.asarray(np.where(load<90)[0]).size
loadFG = load[where]
mean = loadFG.mean()
std = loadFG.std()
f.write('Familiar Cues with GPi:  \t' + str(mean) + ' +/- ' + str(std) + '\n')

file = folder + '/total_good_UnFam_GPi.npy'
load = np.load(file)
loadUFG = load[where]
mean = loadUFG.mean()
std = loadUFG.std()
f.write('Unfamiliar Cues with GPi:  \t' + str(mean) + ' +/- ' + str(std) + '\n')

file =folder + '/total_good_Fam.npy'
load = np.load(file)
#print load
loadF = load[where]
mean = loadF.mean()
std = loadF.std()
bad2 = np.asarray(np.where(load<90)[0]).size
f.write('Familiar Cues without GPi:  \t' + str(mean) + ' +/- ' + str(std) + '\n')

file = folder + '/total_good_UnFam.npy'
load = np.load(file)
loadUF = load[where]
mean = loadUF.mean()
std = loadUF.std()
f.write('Unfamiliar Cues without GPi:  \t' + str(mean) + ' +/- ' + str(std) + '\n\n\n')

f.write('Bad ones with GPi: \t' + str(bad) + '\n')
f.write('Bad ones without GPi: \t' + str(bad) + '\n')

f.close()

fig = plt.figure(figsize=(10,4))
plt.boxplot([loadFG[:], loadUFG[:], loadF[:], loadUF[:]])
plt.ylabel("Performance (%)")
plt.xticks([1, 2, 3, 4], ["Habitual Condition\nwith GPi", "Novelty Condition \nwith GPi","Habitual Condition \nwithout GPi", "Novelty Condition \nwithout GPi"])
plt.ylim(0.0,110.0)
plt.yticks([0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.])

file = folder + "/Performance.png"
fig.savefig(file)

fig = plt.figure()
trials = np.linspace(1, loadFG.size, loadFG.size)
plt.plot(trials,loadFG/100, '*')
plt.plot(trials,loadUFG/100, '--')
plt.plot(trials,loadF/100, 'o')
plt.plot(trials,loadUF/100)
plt.ylim(0.0, 1.1)
plt.show()
# If the cortex learn more the BG the choice is faster without the BG
# The random weights of unfamiliar cues are better for the bad answer
# 	then the choice without BG is faster
# In familiar cues, the cognitive choice is much faster than the motor (~200ms)
#	In unfamiliar ones, it's faster but not that much (~10ms)
