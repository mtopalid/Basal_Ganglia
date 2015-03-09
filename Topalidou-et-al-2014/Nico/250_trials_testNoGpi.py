# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License.
#
# Contributors: Nicolas P. Rougier (Nicolas.Rougier@inria.fr)
# -----------------------------------------------------------------------------
# References:
#
# * Interaction between cognitive and motor cortico-basal ganglia loops during
#   decision making: a computational study. M. Guthrie, A. Leblois, A. Garenne,
#   and T. Boraud. Journal of Neurophysiology, 109:3025–3040, 2013.
# -----------------------------------------------------------------------------
import numpy as np
from model import *
from display import *
from learning import *
from testing import *
import os
from parameters import *



if __name__ == "__main__":

	path = 'Results_SameNoise_InitW_120tr_test'
	if not os.path.exists(path):
		os.makedirs(path)
	debugging = path + '/Debugging.txt'#.txt'
	f = open(debugging, 'wb')

	Ptotal = np.zeros((simulations, n_trials))
	Dtotal = np.zeros(simulations)
	RPtotal = np.zeros((simulations, n))
	APtotal = np.zeros((simulations, n))
	CVtotal = np.zeros((simulations, n))
	mBctotal = np.zeros(simulations)
	ABCtotal = np.zeros(simulations)
	Wtotal = np.zeros((simulations, n))
	NoMovetotal = np.zeros(simulations)

	Ptest = np.zeros((simulations, n_trials))
	Dtest = np.zeros(simulations)
	APtest = np.zeros((simulations, n))
	mBctest = np.zeros(simulations)
	ABCtest = np.zeros(simulations)
	NoMovetest = np.zeros(simulations)

	PtestNoGPi = np.zeros((simulations, n_trials))
	DtestNoGPi = np.zeros(simulations)
	APtestNoGPi = np.zeros((simulations, n))
	mBctestNoGPi = np.zeros(simulations)
	ABCtestNoGPi = np.zeros(simulations)
	NoMovetestNoGPi = np.zeros(simulations)
	for i in range(simulations):
		print 'Experiment: ', i + 1
		reset()
		hist, Ptotal[i,:], Dtotal[i], RPtotal[i,:], APtotal[i,:], mBctotal[i], ABCtotal[i], NoMovetotal[i] = learning_trials(f = f, debugging = False, save = True)
		CVtotal[i, :] = CUE["value"]
		Wtotal[i,:] = connections["CTX.cog -> STR.cog"].weights
		print '-----------------Testing Phase----------------'
		f.write('\n-----------------Testing Phase----------------')
		hist, Ptest[i,:], Dtest[i], APtest[i,:], mBctest[i], ABCtest[i], NoMovetest[i] = testing_trials(f = f, debugging = False, save = True)
		print
		print '-----------------Testing Phase No GPi----------------'
		f.write('\n-----------------Testing Phase----------------')
		connections["GPI.cog -> THL.cog"].active = False
		connections["GPI.mot -> THL.mot"].active = False
		hist, PtestNoGPi[i,:], DtestNoGPi[i], APtestNoGPi[i,:], mBctestNoGPi[i], ABCtestNoGPi[i], NoMovetestNoGPi[i] = testing_trials(f = f, debugging = False, save = True)
		print
		print
		connections["GPI.cog -> THL.cog"].active = True
		connections["GPI.mot -> THL.mot"].active = True

	f.write('\n\n\n')
	debug_total(f, Ptotal, Dtotal, ABCtotal, NoMovetotal, RPtotal, CVtotal, Wtotal, APtotal)
	f.close()

	plt.plot(np.arange(n_trials), np.sum(Ptotal, axis = 0)/simulations*100.)
	plt.show()
	plt.plot(np.arange(n_trials), np.sum(Ptest, axis = 0)/simulations*100.)
	plt.show()
	plt.plot(np.arange(n_trials), np.sum(PtestNoGPi, axis = 0)/simulations*100.)
	plt.show()
	file = path + '/NoMove.npy'
	np.save(file,NoMovetotal)
	file = path + '/Performance.npy'
	np.save(file,Ptotal)
	file = path + '/DifferentChoices.npy'
	np.save(file,Dtotal)
	file = path + '/RewardProbabilities.npy'
	np.save(file,RPtotal)
	file = path + '/MeanCuesValues.npy'
	np.save(file,CVtotal)
	file = path + '/MotBefCog.npy'
	np.save(file,mBctotal)
	file = path + '/ActBefCues.npy'
	np.save(file,ABCtotal)
	file = path + '/Weights.npy'
	np.save(file,Wtotal)

	file = path + '/NoMove-test.npy'
	np.save(file,NoMovetest)
	file = path + '/Performance-test.npy'
	np.save(file,Ptest)
	file = path + '/DifferentChoices-test.npy'
	np.save(file,Dtest)
	file = path + '/MotBefCog-test.npy'
	np.save(file,mBctest)
	file = path + '/ActBefCues-test.npy'
	np.save(file,ABCtest)

	file = path + '/NoMove-test-NoGPi.npy'
	np.save(file,NoMovetestNoGPi)
	file = path + '/Performance-test-NoGPi.npy'
	np.save(file,PtestNoGPi)
	file = path + '/DifferentChoices-test-NoGPi.npy'
	np.save(file,DtestNoGPi)
	file = path + '/MotBefCog-test-NoGPi.npy'
	np.save(file,mBctestNoGPi)
	file = path + '/ActBefCues-test-NoGPi.npy'
	np.save(file,ABCtestNoGPi)
