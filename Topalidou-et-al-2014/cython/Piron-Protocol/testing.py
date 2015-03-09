import numpy as np
import random
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2014/cython/')
from model import *
from display import *
from single_trial import *
from learning import *

def sigmoid(V,Vmin=Vmin,Vmax=Vmax,Vh=Vh,Vc=Vc):
    return  Vmin + (Vmax-Vmin)/(1.0+np.exp((Vh-V)/Vc))

def testing_trials(f = None, n_trials = n_trials, debugging = True, save = False, protocol = 'Piron', familiar = True):
	P, R, D, mBc, ABC, NoMove, RT = [], [], [], [], [], [], [] # ABC: Activity before cues
	RP = np.zeros(4)
	AP = np.zeros(4)
	for j in range(n_trials):
		if debugging:
			print 'Trial: ', j + 1
		time = single_trial(f = f, trial = j, learn = False, protocol = protocol, familiar = familiar, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
		RT.append(time)
		if not len(P) == j+1:
			P.append(0)
	debug(f = f, RT =RT, P = P, D = D, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	print
	if save:
		return P, RT, np.array(D).mean(), AP, np.array(mBc).mean(), np.array(ABC).mean(), len(NoMove)/float(n_trials)
	return hist

if __name__ == "__main__":

	reset(protocol = 'Piron')
	print 'Learning Phase'
	hist = learning_trials(n_trials = 60, debugging = False, protocol = 'Piron', familiar = True)
	connections["GPI.cog -> THL.cog"].active = False
	connections["GPI.mot -> THL.mot"].active = False
	print 'Testing Familiar without GPi'
	hist = testing_trials(n_trials = 60, debugging = False)
	print 'Testing UnFamiliar without GPi'
	hist = testing_trials(hist = True, n_trials = 60, debugging = False, familiar = False)
	#if 1: display_ctx(hist, 3.0)
	connections["GPI.cog -> THL.cog"].active = True
	connections["GPI.mot -> THL.mot"].active = True
	print 'Testing Familiar'
	hist = testing_trials(hist = True, n_trials = 60, debugging = False)
	print 'Testing UnFamiliar'
	hist = learning_trials(n_trials = 60, debugging = False, familiar = False)
	#if 1: display_ctx(hist, 3.0)
