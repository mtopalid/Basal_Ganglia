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
import os
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')
from model import *
from display import *
from learning import *
from testing import *
from parameters import *



if __name__ == "__main__":

	path = 'Results'
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
	for i in range(simulations):
		print 'Experiment: ', i + 1
		reset()
		hist, Ptotal[i,:], Dtotal[i], RPtotal[i,:], APtotal[i,:], mBctotal[i], ABCtotal[i], NoMovetotal[i] = learning_trials(f = f, debugging = False, save = True)
		CVtotal[i, :] = CUE["value"]
		Wtotal[i,:] = connections["CTX.cog -> STR.cog"].weights
		if 0:
			print '-----------------Testing Phase----------------'
			f.write('\n-----------------Testing Phase----------------')
			hist, Ptest[i,:], Dtest[i], APtest[i,:], mBctest[i], ABCtest[i], NoMovetest[i] = testing_trials(f = f, debugging = False, save = True)
		print
		print

	f.write('\n\n\n')
	debug_total(f, Ptotal, Dtotal, ABCtotal, NoMovetotal, RPtotal, CVtotal, Wtotal, APtotal)
	f.close()

	plt.plot(np.arange(n_trials), np.sum(Ptotal, axis = 0)/simulations*100.)
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
