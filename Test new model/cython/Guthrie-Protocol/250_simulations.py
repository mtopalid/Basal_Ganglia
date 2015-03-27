import numpy as np
import os
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Test new model/cython/')
from model import *
from learning import *
from testing import *
from parameters import *





########### Play with cue values and reward in error at learning##############








if __name__ == "__main__":

	inverse = input('\nDo you want to have an inverse of Probabilities during the simulation?\nChoose 1 for True or 0 for False\n')
	path = 'Results'
	if inverse:
		inverse_trial = input('\nAfter how many trials will be the inverse?\n')
		inverse_all = input('\nDo you want to inverse all probabilities or just the middle ones?\nChoose 1 for all or 0 for middle ones\n')
		path += '-inverse-after' + str(inverse_trial)
		path += 'all' if inverse_all else 'middle cues'#-NoCortLearn-HalfParam
	else:
		inverse_trial = 0
		inverse_all = 0
	if not os.path.exists(path):
		os.makedirs(path)
	debugging = path + '/Debugging.txt'#.txt'
	#f = open(debugging, 'wb')


	CVtotal = np.zeros((simulations, n))
	WtotaldSTR = np.zeros((simulations, n_trials, n))
	WtotaliSTR = np.zeros((simulations, n_trials, n))
	WtotalCog = np.zeros((simulations, n_trials, n))
	WtotalMot = np.zeros((simulations, n_trials, n))

	P = np.zeros((simulations, n_trials))
	RT = np.zeros((simulations, n_trials))
	D = np.zeros(simulations)
	RP = np.zeros((simulations, n))
	AP = np.zeros((simulations, n))
	mBc = np.zeros(simulations)
	ABC = np.zeros(simulations)
	NoMove = np.zeros(simulations)


	for i in range(simulations):
		print 'Experiment: ', i + 1
		reset(protocol = 'Guthrie')

		P[i,:], RT[i,:], D[i], RP[i,:], AP[i,:], mBc[i], ABC[i], NoMove[i], WtotalCog[i], WtotalMot[i], WtotaldSTR[i], WtotaliSTR[i] = learning_trials(inversable = inverse, inverse_all = inverse_all, inverse_trial = inverse_trial, protocol = 'Guthrie', trials = n_trials, debugging = False, save = True)

		CVtotal[i, :] = CUE["value"]
		print
		print

	debug_total(P, D, ABC, NoMove, AP, RP, CVtotal, WtotalCog, WtotalMot, WtotaldSTR, WtotaliSTR)
	#f.close()

	file = path + '/MeanCuesValues.npy'
	np.save(file,CVtotal)
	file = path + '/Weights_dStr.npy'
	np.save(file,WtotaldSTR)
	file = path + '/Weights_iStr.npy'
	np.save(file,WtotaliSTR)
	file = path + '/Weights_Cog.npy'
	np.save(file,WtotalCog)
	file = path + '/Weights_Mot.npy'
	np.save(file,WtotalMot)

	file = path + '/NoMove.npy'
	np.save(file,NoMove)
	file = path + '/RT.npy'
	np.save(file,RT)
	file = path + '/Performance.npy'
	np.save(file,P)
	file = path + '/DifferentChoices.npy'
	np.save(file,D)
	file = path + '/MotBefCog.npy'
	np.save(file,mBc)
	file = path + '/ActBefCues.npy'
	np.save(file,ABC)
