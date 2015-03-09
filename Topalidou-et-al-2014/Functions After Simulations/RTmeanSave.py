import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2014/cython/')

from parameters import *

protocol = input('Choose 1 for Guthrie-Protocol or 2 for Piron-Protocol\n')
if protocol == 1:
	folder = '../../../Results/Topalidou-et-al-2014/cython/Guthrie-Protocol/Results'
elif protocol == 2:
	folder = '../../../Results/Topalidou-et-al-2014/cython/Piron-Protocol/Results120-120-HalfLearningPar-50'#


RTmean = folder + '/RTmean.txt'#.txt'
f = open(RTmean, 'wb')

f.write('Motor:\n\n')

file = folder + '/delete.npy'
delete = np.load(file)
f.write('Number of trials with bad learning: %d \n\n' %len(delete))

file = folder + '/RT-fam.npy'
#loadFG = np.load(file)
load = np.load(file)
loadFG = np.delete(load, delete,0)
mean0 = loadFG[:].mean()
std0 = loadFG[:].std()
#mean1 = loadFG[:,1].mean()
#std1 = loadFG[:,1].std()
f.write('Familiar Cues with GPi:		%.3f +/- %.3f\n\n' %(mean0, std0))

file = folder + '/RT-unfam.npy'
#loadUFG = np.load(file)
load = np.load(file)
loadUFG = np.delete(load, delete,0)
mean0 = loadUFG[:,0].mean()
std0 = loadUFG[:,0].std()
#mean1 = loadUFG[:,1].mean()
#std1 = loadUFG[:,1].std()
f.write('UnFamiliar Cues with GPi: %.3f +/- %.3f\n\n' %(mean0, std0))# + '\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1)

file = folder + '/RT-fam_NoGPi.npy'
#loadF = np.load(file)
load = np.load(file)
loadF = np.delete(load, delete,0)
mean0 = loadF[:,0].mean()
std0 = loadF[:,0].std()
#mean1 = loadF[:,1].mean()
#std1 = loadF[:,1].std()
f.write('Familiar Cues without GPi:	%.3f +/- %.3f\n\n' %(mean0, std0))

file = folder + '/RT-unfam_NoGPi.npy'
#loadUF = np.load(file)
load = np.load(file)
loadUF = np.delete(load, delete,0)
mean0 = loadUF[:,0].mean()
std0 = loadUF[:,0].std()
#mean1 = loadUF[:,1].mean()
#std1 = loadUF[:,1].std()
f.write('UnFamiliar Cues without GPi: %.3f +/- %.3f\n\n' %(mean0, std0))

if 0:
	f.write('\n\n\nCognitive:\n\n')

	file = m.rt + '/Fam_GPi_cog.npy'
	load = np.load(file)
	load = load[good_ones,:]
	mean0 = load[:,0].mean()
	std0 = load[:,0].std()
	mean1 = load[:,1].mean()
	std1 = load[:,1].std()
	f.write('Familiar Cues with GPi cog:  \tmean: ' + str(mean0) + ' +/- ' + str(std0) +
			'\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1) + '\n\n')
	file = m.rt + '/UnFam_GPi_cog.npy'
	load = np.load(file)
	load = load[good_ones,:]
	mean0 = load[:,0].mean()
	std0 = load[:,0].std()
	mean1 = load[:,1].mean()
	std1 = load[:,1].std()
	f.write('UnFamiliar Cues with GPi cog:  \tmean: ' + str(mean0) + ' +/- ' + str(std0) +
			'\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1) + '\n\n')
	file = m.rt + '/Fam_cog.npy'
	load = np.load(file)
	load = load[good_ones,:]
	mean0 = load[:,0].mean()
	std0 = load[:,0].std()
	mean1 = load[:,1].mean()
	std1 = load[:,1].std()
	f.write('Familiar Cues without GPi cog:  \tmean: ' + str(mean0) + ' +/- ' + str(std0) +
			'\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1) + '\n\n')
	file = m.rt + '/UnFam_cog.npy'
	load = np.load(file)
	load = load[good_ones,:]
	mean0 = load[:,0].mean()
	std0 = load[:,0].std()
	mean1 = load[:,1].mean()
	std1 = load[:,1].std()
	f.write('UnFamiliar Cues without GPi cog:  \tmean: ' + str(mean0) + ' +/- ' + str(std0) +
			'\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1) + '\n\n')
f.close()

fig = plt.figure(figsize=(10,4))
plt.boxplot([loadFG[:,0], loadUFG[:,0], loadF[:,0], loadUF[:,0]])
plt.ylabel("Reaction Time (ms)")
plt.xticks([1, 2, 3, 4], ["Habitual Condition\nwith GPi", "Novelty Condition \nwith GPi","Habitual Condition \nwithout GPi", "Novelty Condition \nwithout GPi"])

file = folder + "/ResponseTime.png"
fig.savefig(file)
plt.show()
