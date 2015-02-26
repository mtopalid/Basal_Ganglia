import numpy as np
import os

def initial_arrays2save(simulations, testing_trials):

	RTmean_Fam_GPi = np.zeros((simulations,2))
	RTmean_UnFam_GPi = np.zeros((simulations,2))
	RTmean_Fam = np.zeros((simulations,2))
	RTmean_UnFam = np.zeros((simulations,2))
	Pmean_Fam_GPi = np.zeros((simulations,1))
	Pmean_UnFam_GPi = np.zeros((simulations,1))
	Pmean_Fam = np.zeros((simulations,1))
	Pmean_UnFam = np.zeros((simulations,1))
	P_Fam_GPi = np.zeros((simulations,testing_trials))
	P_UnFam_GPi = np.zeros((simulations,testing_trials))
	P_Fam = np.zeros((simulations,testing_trials))
	P_UnFam = np.zeros((simulations,testing_trials))
	return RTmean_Fam_GPi,RTmean_UnFam_GPi,RTmean_Fam,RTmean_UnFam,Pmean_Fam_GPi,Pmean_UnFam_GPi,Pmean_Fam,Pmean_UnFam,P_Fam_GPi,P_UnFam_GPi,P_Fam,P_UnFam

def save_2_arrays(D, P):

	d = D[np.nonzero(D)]
	RTmean = np.array([d.mean(), d.std()])
	Pmean = float(np.sum(P))/len(P)*100

	return RTmean, Pmean, P

def save_Guthrie(path,LearningOptimumTrials):

	if not os.path.exists(path):
		os.makedirs(path)

	file = folder + path + '/LearningOptimumTrials.npy'
	np.save(file,LearningOptimumTrials)

def save_in_files(path, RTmean_Fam_GPi,RTmean_UnFam_GPi,RTmean_Fam,RTmean_UnFam,Pmean_Fam_GPi,Pmean_UnFam_GPi,Pmean_Fam,Pmean_UnFam,P_Fam_GPi,P_UnFam_GPi,P_Fam,P_UnFam,LearningOptimumTrials):

	if not os.path.exists(path):
		os.makedirs(path)

	file = path + '/Fam_GPi.npy'
	np.save(file,RTmean_Fam_GPi)
	file = path + '/UnFam_GPi.npy'
	np.save(file,RTmean_UnFam_GPi)
	file = path + '/Fam.npy'
	np.save(file,RTmean_Fam)
	file = path + '/UnFam.npy'
	np.save(file,RTmean_UnFam)

	file = path + '/total_good_Fam_GPi.npy'
	np.save(file,Pmean_Fam_GPi)
	file = path + '/total_good_UnFam_GPi.npy'
	np.save(file,Pmean_UnFam_GPi)
	file = path + '/total_good_Fam.npy'
	np.save(file,Pmean_Fam)
	file = path + '/total_good_UnFam.npy'
	np.save(file,Pmean_UnFam)

	file = path + '/good_Fam_GPi.npy'
	np.save(file,P_Fam_GPi)
	file = path + '/good_UnFam_GPi.npy'
	np.save(file,P_UnFam_GPi)
	file = path + '/good_Fam.npy'
	np.save(file,P_Fam)
	file = path + '/good_UnFam.npy'
	np.save(file,P_UnFam)

	file = path + '/LearningOptimumTrials.npy'
	np.save(file,LearningOptimumTrials)
