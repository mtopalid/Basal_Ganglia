import numpy as np
import os
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia_Model/')
import parameters_Nico as p

file = p.rt + '/good_Fam_GPi.npy'
loadFG = np.load(file)

file = p.rt + '/good_UnFam_GPi.npy'
loadUFG = np.load(file)

file = p.rt + '/good_Fam.npy'
loadF = np.load(file)

file = p.rt + '/good_UnFam.npy'
loadUF = np.load(file)

if (loadFG==0).any():
	delete = np.where(loadFG==0)[0][0]
	loadFG = np.delete(loadFG, delete,0)
	loadUFG = np.delete(loadUFG, delete,0)
	loadF = np.delete(loadF, delete,0)
	loadUF = np.delete(loadUF, delete,0)

MeanRateFG	 = np.zeros(loadFG.shape[1])
MeanRateUFG	 = np.zeros(loadUFG.shape[1])
MeanRateF	 = np.zeros(loadF.shape[1])
MeanRateUF	 = np.zeros(loadUF.shape[1])
for i in range(loadFG.shape[0]):
	MeanRateFG	 += loadFG[i,:]
	MeanRateUFG	 += loadUFG[i,:]
	MeanRateF	 += loadF[i,:]
	MeanRateUF	 += loadUF[i,:]
MeanRateFG	 = MeanRateFG/loadFG.shape[0]
MeanRateUFG	 = MeanRateUFG/loadUFG.shape[0]
MeanRateF	 = MeanRateF/loadF.shape[0]
MeanRateUF	 = MeanRateUF/loadUF.shape[0]
fig = plt.figure(figsize=(15,8), frameon = False)
plt.plot(MeanRateFG,'b--', label = 'HC with GPi')
plt.plot(MeanRateUFG,'r--', label = 'NC with GPi')
plt.plot(MeanRateF,'g', label = 'HC without GPi')
plt.plot(MeanRateUF,'m', label = 'NC without GPi')
plt.ylabel("Mean Rate Success")
plt.xlabel("Number of Trials")
plt.legend(frameon=False, loc='lower right')
plt.ylim(0.0,1.01)
file = p.rt + "/MeanRateSuccess.png"
fig.savefig(file)


plt.show()
# If the cortex learn more the BG the choice is faster without the BG
# The random weights of unfamiliar cues are better for the bad answer
# 	then the choice without BG is faster
# In familiar cues, the cognitive choice is much faster than the motor (~200ms)
#	In unfamiliar ones, it's faster but not that much (~10ms)
