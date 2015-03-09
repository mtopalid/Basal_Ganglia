import numpy as np
import random
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')
from model import *
from display import *
from single_trial import *
from parameters import *


def learning_trials(f = None, trials = n_trials, debugging = True, save = False, protocol = 'Piron', familiar = True, type = 'learning'):
	P, R, D, mBc, ABC, NoMove, RT = [], [], [], [], [], [], []
	RP = np.zeros(n)
	AP = np.zeros(n)
	trained = False
	tr = 0
	while not trained and tr<trials:
		#for j in range(n_trials):
		if debugging:
			print 'Trial: ', tr + 1
		if save:
			time = single_trial(f = f, trial = tr, learn = True, protocol = protocol, familiar = familiar, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
		else:
			hist, time = single_trial(f = f, trial = tr, learn = True, protocol = protocol, familiar = familiar, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
		RT.append(time)
		if not len(P) == tr+1:
			P.append(0)
		if type == 'learning':
			if np.mean(P[-n_Performance:]) > 0.9 and tr > n_Performance:
				trained = True
		tr += 1

	debug(f = f, RT = RT, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	debug_learning(connections["CTX.cog -> CTX.ass"].weights, connections["CTX.mot -> CTX.ass"].weights, connections["CTX.cog -> STR.cog"].weights, cues_value = CUE["value"], f = f)
	print
	if save:
		return P, RT, np.array(D).mean(), RP, AP, np.array(mBc).mean(), np.array(ABC).mean(), len(NoMove)/float(n_trials)
	return hist

if __name__ == "__main__":

	reset(protocol = 'Piron')
	hist, P = learning_trials(hist = True)
	#if 1: display_ctx(hist, 3.0)
