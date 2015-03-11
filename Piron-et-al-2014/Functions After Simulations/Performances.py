import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Piron-et-al-2014/cython/')

from parameters import *

def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c
protocol = input('Choose 1 for Guthrie-Protocol or 2 for Piron-Protocol\n')
if protocol == 1:
	folder = '../cython/Guthrie-Protocol/Results'
	file = folder + '/Performance.npy'
	load = np.load(file)
	if 0:
		delete = []
		for i in range (load.shape[0]):
			if load[i,:].mean()<0.90:
				delete.append(i)
		print 'Number of trials with bad learning: ', len(delete)
		file = folder+ '/delete.npy'
		np.save(file, delete)

		load = np.delete(load, delete,0)
	mean =  load.mean(axis = 0).mean()*100#
	Optimum_trials = np.zeros(load.shape[1])
	for i in range(0,load.shape[0],1):
		Optimum_trials += load[i,:]

	Optimum_trials = Optimum_trials/float(load.shape[0])
	file = folder+ '/OptimumTrials.npy'
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
	plt.title('Habitual Condition \nMean Performance: %.3f %%' % (mean))#of 10 last trials
	file = folder + "/LearningCurve.png"
	fig.savefig(file)
	plt.show()

elif protocol == 2:
	folder = '../../../Results/Topalidou-et-al-2015/cython/Piron-Protocol/Results'#
	#path = 'Piron-Protocol/Results-HalfLearningPar'
	file = folder + '/Performance-fam.npy'
	load = np.load(file)
	delete = []
	for i in range (load.shape[0]):
		if load[i,:].mean()<0.90:
			delete.append(i)
	print 'Number of trials with bad learning: ', len(delete)
	file = folder+ '/delete.npy'
	np.save(file, delete)

	load = np.delete(load, delete,0)
	mean =  load.mean(axis = 0).mean()#
	Optimum_trials = np.zeros(load.shape[1])
	for i in range(0,load.shape[0],1):
		Optimum_trials += load[i,:]

	Optimum_trials = Optimum_trials/float(load.shape[0])
	file = folder+ '/OptimumTrials-fam.npy'
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
	plt.title('Habitual Condition \nMean Performance: %.3f %%\nNumber of trials with bad learning: %d' % (mean, len(delete)))#of 10 last trials
	file = folder + "/LearningCurve-fam.png"
	fig.savefig(file)



	file = folder + '/Performance-unfam.npy'
	load = np.load(file)
	load = np.delete(load, delete,0)
	mean =  load.mean(axis = 0).mean()#
	Optimum_trials = np.zeros(load.shape[1])
	for i in range(0,load.shape[0],1):
		Optimum_trials += load[i,:]

	Optimum_trials = Optimum_trials/float(load.shape[0])
	file = folder+ '/OptimumTrials-unfam.npy'
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
	plt.title('Novelty Condition \nMean Performance: %.3f %%' %mean)#of 10 last trials
	file = folder + "/LearningCurve-unfam.png"
	fig.savefig(file)


	file = folder + '/Performance-fam_NoGPi.npy'
	load = np.load(file)
	load = np.delete(load, delete,0)
	mean =  load.mean(axis = 0).mean()#
	Optimum_trials = np.zeros(load.shape[1])
	for i in range(0,load.shape[0],1):
		Optimum_trials += load[i,:]

	Optimum_trials = Optimum_trials/float(load.shape[0])
	file = folder+ '/OptimumTrials-fam_NoGPi.npy'
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
	plt.title('Habitual Condition without GPi \nMean Performance: %.3f %%' %mean)#of 10 last trials
	file = folder + "/LearningCurve-fam_NoGPi.png"
	fig.savefig(file)


	file = folder + '/Performance-unfam_NoGPi.npy'
	load = np.load(file)
	load = np.delete(load, delete,0)
	mean =  load.mean(axis = 0).mean()#
	Optimum_trials = np.zeros(load.shape[1])
	for i in range(0,load.shape[0],1):
		Optimum_trials += load[i,:]

	Optimum_trials = Optimum_trials/float(load.shape[0])
	file = folder+ '/OptimumTrials-unfam_NoGPi.npy'
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
	plt.title('Novelty Condition without GPi \nMean Performance: %.3f %%' %mean)#of 10 last trials
	file = folder + "/LearningCurve-unfam_NoGPi.png"
	fig.savefig(file)
	plt.show()
