import numpy as np
import os
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')
from model import *
from learning import *
from testing import *
from parameters import *



if __name__ == "__main__":

	path = 'Results'#
	if not os.path.exists(path):
		os.makedirs(path)
	debugging = path + '/Debugging.txt'#.txt'
	f = open(debugging, 'wb')


	CVtotal = np.zeros((simulations, n))
	WtotalSTR = np.zeros((simulations, n))
	WtotalCog = np.zeros((simulations, n))
	WtotalMot = np.zeros((simulations, n))

	P = np.zeros((simulations, n_testing_trials))
	RT = np.zeros((simulations, n_testing_trials))
	D = np.zeros(simulations)
	RP = np.zeros((simulations, n))
	AP = np.zeros((simulations, n))
	mBc = np.zeros(simulations)
	ABC = np.zeros(simulations)
	NoMove = np.zeros(simulations)


	for i in range(simulations):
		print 'Experiment: ', i + 1
		reset(protocol = 'Guthrie')

		P[i,:], RT[i,:], D[i], RP[i,:], AP[i,:], mBc[i], ABC[i], NoMove[i] = learning_trials(protocol = 'Guthrie', trials = n_testing_trials, f = f, debugging = False, save = True)

		CVtotal[i, :] = CUE["value"]
		WtotalSTR[i,:] = connections["CTX.cog -> STR.cog"].weights
		WtotalCog[i,:] = connections["CTX.cog -> CTX.ass"].weights
		WtotalMot[i,:] = connections["CTX.mot -> CTX.ass"].weights
		print
		print

	debug_total(f, P, D, ABC, NoMove, AP, RP, CVtotal, WtotalSTR, WtotalCog, WtotalMot)
	f.close()

	file = path + '/MeanCuesValues.npy'
	np.save(file,CVtotal)
	file = path + '/Weights_Str.npy'
	np.save(file,WtotalSTR)
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
