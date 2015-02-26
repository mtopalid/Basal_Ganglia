import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia_Model/')
import parameters_Nico as p


RTmean = p.rt + '/RTmean-withoutBad.txt'#.txt'
f = open(RTmean, 'wb')

f.write('Motor:\n\n')

file = p.rt + '/total_good_Fam_GPi.npy'
load = np.load(file)
good_ones = np.where(load>90)[0]
file = p.rt + '/Fam_GPi.npy'
#loadFG = np.load(file)
load = np.load(file)
loadFG = load[good_ones,:]
mean0 = loadFG[:,0].mean()
std0 = loadFG[:,0].std()
mean1 = loadFG[:,1].mean()
std1 = loadFG[:,1].std()
f.write('Familiar Cues with GPi:  \tmean: ' + str(mean0) + ' +/- ' + str(std0) +
		'\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1) + '\n\n')

file = p.rt + '/UnFam_GPi.npy'
loadUFG = np.load(file)
load = np.load(file)
loadUFG = load[good_ones,:]
mean0 = loadUFG[:,0].mean()
std0 = loadUFG[:,0].std()
mean1 = loadUFG[:,1].mean()
std1 = loadUFG[:,1].std()
f.write('UnFamiliar Cues with GPi:  \tmean: ' + str(mean0) + ' +/- ' + str(std0) +
		'\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1) + '\n\n')

file = p.rt + '/total_good_Fam.npy'
load = np.load(file)
good_ones2 = np.where(load>90)[0]
file = p.rt + '/Fam.npy'
loadF = np.load(file)
load = np.load(file)
loadF = load[good_ones,:]
mean0 = loadF[:,0].mean()
std0 = loadF[:,0].std()
mean1 = loadF[:,1].mean()
std1 = loadF[:,1].std()
f.write('Familiar Cues without GPi:  \tmean: ' + str(mean0) + ' +/- ' + str(std0) +
		'\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1) + '\n\n')
file = p.rt + '/UnFam.npy'
loadUF = np.load(file)
load = np.load(file)
loadUF = load[good_ones,:]
mean0 = loadUF[:,0].mean()
std0 = loadUF[:,0].std()
mean1 = loadUF[:,1].mean()
std1 = loadUF[:,1].std()
f.write('UnFamiliar Cues without GPi:  \tmean: ' + str(mean0) + ' +/- ' + str(std0) +
		'\n\t\t\t\tstd: ' + str(mean1) + ' +/- ' + str(std1) + '\n\n')

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
plt.boxplot([loadFG[:,0]*1000, loadUFG[:,0]*1000, loadF[:,0]*1000, loadUF[:,0]*1000])
plt.ylabel("Reaction Time (ms)")
plt.xticks([1, 2, 3, 4], ["Habitual Condition\nwith GPi", "Novelty Condition \nwith GPi","Habitual Condition \nwithout GPi", "Novelty Condition \nwithout GPi"])

file = p.rt + "/ResponseTime.png"
fig.savefig(file)
#plt.show()
