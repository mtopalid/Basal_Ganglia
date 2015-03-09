import numpy as np
import os
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2014/cython/')
from model import *
from display import *
from learning import *
from testing import *
from parameters import *



if __name__ == "__main__":

	path = 'Results-test-learning'
	if not os.path.exists(path):
		os.makedirs(path)
	debugging = path + '/Debugging.txt'#.txt'
	f = open(debugging, 'wb')
	simulations = 100

	Ptest_learning = np.zeros((simulations, 50))
	Ptest_fam = np.zeros((simulations, 20))
	Ptest_unfam = np.zeros((simulations, 5))
	Ptest_fam_NoGPi = np.zeros((simulations, 20))
	Ptest_unfam_NoGPi = np.zeros((simulations, 20))
	for i in range(simulations):
		print 'Experiment: ', i + 1
		reset(protocol = 'Piron')
		print '-----------------Learning Phase----------------'
		f.write('\n-----------------Learning Phase----------------')
		Ptest_learning[i,:], temp, temp, temp, temp, temp, temp  = learning_trials(n_trials = 50, f = f, debugging = False, save = True, protocol = 'Piron', familiar = True)

		connections["GPI.cog -> THL.cog"].active = False
		connections["GPI.mot -> THL.mot"].active = False
		print '--------Testing Familiar without GPi--------'
		f.write('\n--------Testing Familiar without GPi--------')
		Ptest_fam_NoGPi[i,:], temp, temp, temp, temp, temp = testing_trials(n_trials = 20, f = f, debugging = False, save = True)
		print
		connections["GPI.cog -> THL.cog"].active = True
		connections["GPI.mot -> THL.mot"].active = True
		print '--------Testing Familiar with GPi--------'
		f.write('\n--------Testing Familiar with GPi--------')
		Ptest_fam[i,:], temp, temp, temp, temp, temp, temp = learning_trials(n_trials = 20, f = f, debugging = False, save = True)
		print

		if 0:
			print '-----------------Testing Phase----------------'
			f.write('\n-----------------Testing Phase----------------')


			print '--------Testing UnFamiliar without GPi--------'
			f.write('\n--------Testing UnFamiliar without GPi--------')
			Ptest_unfam_NoGPi[i,:], temp, temp, temp, temp, temp = testing_trials(n_trials = 5, f = f, debugging = False, save = True, familiar = False)

			connections["GPI.cog -> THL.cog"].active = True
			connections["GPI.mot -> THL.mot"].active = True

			print '--------Testing Familiar with GPi--------'
			f.write('\n--------Testing Familiar with GPi--------')
			Ptest_fam[i,:], temp, temp, temp, temp, temp, temp = learning_trials(n_trials = 5, f = f, debugging = False, save = True)
			print

			print '--------Testing UnFamiliar with GPi--------'
			f.write('\n--------Testing UnFamiliar with GPi--------')
			Ptest_unfam[i,:], temp, temp, temp, temp, temp, temp = learning_trials(n_trials = 5, f = f, debugging = False, save = True, familiar = False)
		print
		print


	f.close()

	delete = []
	for i in range (Ptest_fam_NoGPi.shape[0]):
		if Ptest_fam_NoGPi[i,:].mean()<0.90:
			delete.append(i)
	print 'Number of trials with bad learning: ', len(delete)
	print 'Number of trials with bad learning: %.3f %%' % (len(delete)/float(simulations)*100)
	plt.plot(np.sum(Ptest_learning,axis = 0))
	plt.plot(np.sum(Ptest_fam_NoGPi,axis = 0))
	plt.plot(np.sum(Ptest_fam,axis = 0))
	plt.show()


