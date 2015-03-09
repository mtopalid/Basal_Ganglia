
import numpy as np
import os
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')
from model import *
from display import *
from learning import *
from testing import *
from parameters import *



if __name__ == "__main__":

	path = '../../../../Results/Topalidou-et-al-2015/cython/Piron-Protocol/Results120-120-HalfLearningPar-30'#
	if not os.path.exists(path):
		os.makedirs(path)
	debugging = path + '/Debugging.txt'#.txt'
	f = open(debugging, 'wb')


	CVtotal = np.zeros((simulations, n))
	WtotalSTR = np.zeros((simulations, n))
	WtotalCog = np.zeros((simulations, n))
	WtotalMot = np.zeros((simulations, n))

	Ptest_fam = np.zeros((simulations, n_testing_trials))
	RTtest_fam = np.zeros((simulations, n_testing_trials))
	Dtest_fam = np.zeros(simulations)
	RPtest_fam = np.zeros((simulations, n))
	APtest_fam = np.zeros((simulations, n))
	mBctest_fam = np.zeros(simulations)
	ABCtest_fam = np.zeros(simulations)
	NoMovetest_fam = np.zeros(simulations)

	Ptest_unfam = np.zeros((simulations, n_testing_trials))
	RTtest_unfam = np.zeros((simulations, n_testing_trials))
	Dtest_unfam = np.zeros(simulations)
	RPtest_unfam = np.zeros((simulations, n))
	APtest_unfam = np.zeros((simulations, n))
	mBctest_unfam = np.zeros(simulations)
	ABCtest_unfam = np.zeros(simulations)
	NoMovetest_unfam = np.zeros(simulations)

	Ptest_fam_NoGPi = np.zeros((simulations, n_testing_trials))
	RTtest_fam_NoGPi = np.zeros((simulations, n_testing_trials))
	Dtest_fam_NoGPi = np.zeros(simulations)
	APtest_fam_NoGPi = np.zeros((simulations, n))
	mBctest_fam_NoGPi = np.zeros(simulations)
	ABCtest_fam_NoGPi = np.zeros(simulations)
	NoMovetest_fam_NoGPi = np.zeros(simulations)

	Ptest_unfam_NoGPi = np.zeros((simulations, n_testing_trials))
	RTtest_unfam_NoGPi = np.zeros((simulations, n_testing_trials))
	Dtest_unfam_NoGPi = np.zeros(simulations)
	APtest_unfam_NoGPi = np.zeros((simulations, n))
	mBctest_unfam_NoGPi = np.zeros(simulations)
	ABCtest_unfam_NoGPi = np.zeros(simulations)
	NoMovetest_unfam_NoGPi = np.zeros(simulations)
	for i in range(simulations):
		print 'Experiment: ', i + 1
		reset(protocol = 'Piron')
		print '-----------------Learning Phase----------------'
		f.write('\n-----------------Learning Phase----------------')
		learning_trials(trials = n_learning_trials, f = f, debugging = False, save = True, protocol = 'Piron', familiar = True)

		print '-----------------Testing Phase----------------'
		f.write('\n-----------------Testing Phase----------------')
		connections["GPI.cog -> THL.cog"].active = False
		connections["GPI.mot -> THL.mot"].active = False

		print '--------Testing Familiar without GPi--------'
		f.write('\n--------Testing Familiar without GPi--------')
		Ptest_fam_NoGPi[i,:], RTtest_fam_NoGPi[i,:], Dtest_fam_NoGPi[i], APtest_fam_NoGPi[i,:], mBctest_fam_NoGPi[i], ABCtest_fam_NoGPi[i], NoMovetest_fam_NoGPi[i] = testing_trials(n_trials = n_testing_trials, f = f, debugging = False, save = True)
		print

		print '--------Testing UnFamiliar without GPi--------'
		f.write('\n--------Testing UnFamiliar without GPi--------')
		Ptest_unfam_NoGPi[i,:], RTtest_unfam_NoGPi[i,:], Dtest_unfam_NoGPi[i], APtest_unfam_NoGPi[i,:], mBctest_unfam_NoGPi[i], ABCtest_unfam_NoGPi[i], NoMovetest_unfam_NoGPi[i] = testing_trials(n_trials = n_testing_trials, f = f, debugging = False, save = True, familiar = False)

		connections["GPI.cog -> THL.cog"].active = True
		connections["GPI.mot -> THL.mot"].active = True

		print '--------Testing UnFamiliar with GPi--------'
		f.write('\n--------Testing UnFamiliar with GPi--------')
		Ptest_unfam[i,:], RTtest_unfam[i,:], Dtest_unfam[i], RPtest_unfam[i,:], APtest_unfam[i,:], mBctest_unfam[i], ABCtest_unfam[i], NoMovetest_unfam[i] = learning_trials(trials = n_testing_trials, f = f, debugging = False, save = True, familiar = False, type = 'testing')

		print '--------Testing Familiar with GPi--------'
		f.write('\n--------Testing Familiar with GPi--------')
		Ptest_fam[i,:], RTtest_fam[i,:], Dtest_fam[i], RPtest_fam[i,:], APtest_fam[i,:], mBctest_fam[i], ABCtest_fam[i], NoMovetest_fam[i] = learning_trials(trials = n_testing_trials, f = f, debugging = False, save = True, type = 'testing')
		print

		CVtotal[i, :] = CUE["value"]
		WtotalSTR[i,:] = connections["CTX.cog -> STR.cog"].weights
		WtotalCog[i,:] = connections["CTX.cog -> CTX.ass"].weights
		WtotalMot[i,:] = connections["CTX.mot -> CTX.ass"].weights
		print
		print

	f.close()

	file = path + '/MeanCuesValues.npy'
	np.save(file,CVtotal)
	file = path + '/Weights_Str.npy'
	np.save(file,WtotalSTR)
	file = path + '/Weights_Cog.npy'
	np.save(file,WtotalCog)
	file = path + '/Weights_Mot.npy'
	np.save(file,WtotalMot)

	file = path + '/NoMove-fam_NoGPi.npy'
	np.save(file,NoMovetest_fam_NoGPi)
	file = path + '/RT-fam_NoGPi.npy'
	np.save(file,RTtest_fam_NoGPi)
	file = path + '/Performance-fam_NoGPi.npy'
	np.save(file,Ptest_fam_NoGPi)
	file = path + '/DifferentChoices-fam_NoGPi.npy'
	np.save(file,Dtest_fam_NoGPi)
	file = path + '/MotBefCog-fam_NoGPi.npy'
	np.save(file,mBctest_fam_NoGPi)
	file = path + '/ActBefCues-fam_NoGPi.npy'
	np.save(file,ABCtest_fam_NoGPi)

	file = path + '/NoMove-unfam_NoGPi.npy'
	np.save(file,NoMovetest_unfam_NoGPi)
	file = path + '/RT-unfam_NoGPi.npy'
	np.save(file,RTtest_unfam_NoGPi)
	file = path + '/Performance-unfam_NoGPi.npy'
	np.save(file,Ptest_unfam_NoGPi)
	file = path + '/DifferentChoices-unfam_NoGPi.npy'
	np.save(file,Dtest_unfam_NoGPi)
	file = path + '/MotBefCog-unfam_NoGPi.npy'
	np.save(file,mBctest_unfam_NoGPi)
	file = path + '/ActBefCues-unfam_NoGPi.npy'
	np.save(file,ABCtest_unfam_NoGPi)

	file = path + '/NoMove-fam.npy'
	np.save(file,NoMovetest_fam)
	file = path + '/RT-fam.npy'
	np.save(file,RTtest_fam)
	file = path + '/Performance-fam.npy'
	np.save(file,Ptest_fam)
	file = path + '/DifferentChoices-fam.npy'
	np.save(file,Dtest_fam)
	file = path + '/MotBefCog-fam.npy'
	np.save(file,mBctest_fam)
	file = path + '/ActBefCues-fam.npy'
	np.save(file,ABCtest_fam)

	file = path + '/NoMove-unfam.npy'
	np.save(file,NoMovetest_unfam)
	file = path + '/RT-unfam.npy'
	np.save(file,RTtest_unfam)
	file = path + '/Performance-unfam.npy'
	np.save(file,Ptest_unfam)
	file = path + '/DifferentChoices-unfam.npy'
	np.save(file,Dtest_unfam)
	file = path + '/MotBefCog-unfam.npy'
	np.save(file,mBctest_unfam)
	file = path + '/ActBefCues-unfam.npy'
	np.save(file,ABCtest_unfam)
