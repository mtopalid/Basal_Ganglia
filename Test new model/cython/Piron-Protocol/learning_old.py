import numpy as np
import random
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')
from model import *
from display import *
from trial import *
from parameters import *
from dana import *
from learning import *

def learning(f = None, trials = n_trials, debugging = True, save = False, protocol = 'Piron', familiar = True, type = 'learning', hist = False, P = [], R = [], D = [], mBc = [], ABC = [], NoMove = [], RT = [], RP = [], AP = []):

	if save:
		time = single_trial(f = f, trial = trials, learn = True, protocol = protocol, hist = hist, familiar = familiar, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	else:
		histor, time = single_trial(f = f, trial = trials, learn = True, protocol = protocol, hist = hist, familiar = familiar, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	RT.append(time)
	if not len(P) == trials+1:
		P.append(0)
	if save:
		return time, RT, P, D, RP, AP, mBc, ABC, NoMove
	else:
		return histor, time, RT, P, D, RP, AP, mBc, ABC, NoMove

def learning_trials(f = None, trials = n_trials, debugging = True, save = False, protocol = 'Piron', familiar = True, type = 'learning', hist = False):
	trained = False
	while not trained:
		P, R, D, mBc, ABC, NoMove, RT = [], [], [], [], [], [], []
		RP = np.zeros(n)
		AP = np.zeros(n)
		reset(protocol = 'Piron')
		for j in range(20):
			if debugging:
				print 'Trial: ', j + 1
			if save:
				time, RT, P, D, RP, AP, mBc, ABC, NoMove = learning(f = f, trials = j, debugging = debugging, save = save, protocol = protocol, familiar = familiar, type = type, hist = hist, P = P, R = R, D = D, mBc = mBc, ABC = ABC, NoMove = NoMove, RT = RT, RP = RP, AP = AP)
			else:
				histor, time, RT, P, D, RP, AP, mBc, ABC, NoMove = learning(f = f, trials = j, debugging = debugging, save = save, protocol = protocol, familiar = familiar, type = type, hist = hist, P = P, R = R, D = D, mBc = mBc, ABC = ABC, NoMove = NoMove, RT = RT, RP = RP, AP = AP)

		if type == 'learning':
			if np.mean(P) > 0.70:
				trained = True
		else:
			trained = True
	else:
		for i in range(n_trials-20):
			if debugging:
				print 'Trial: ', i + j + 2
			if save:
				time, RT, P, D, RP, AP, mBc, ABC, NoMove = learning(f = f, trials = i + j + 2, debugging = debugging, save = save, protocol = protocol, familiar = familiar, type = type, hist = hist, P = P, R = R, D = D, mBc = mBc, ABC = ABC, NoMove = NoMove, RT = RT, RP = RP, AP = AP)
			else:
				histor, time, RT, P, D, RP, AP, mBc, ABC, NoMove = learning(f = f, trials = i + j + 2, debugging = debugging, save = save, protocol = protocol, familiar = familiar, type = type, hist = hist, P = P, R = R, D = D, mBc = mBc, ABC = ABC, NoMove = NoMove, RT = RT, RP = RP, AP = AP)
	debug(f = f, RT = RT, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	debug_learning(connections["CTX.cog -> CTX.ass"].weights, connections["CTX.mot -> CTX.ass"].weights, connections["CTX.cog -> STR.cog"].weights, cues_value = CUE["value"], f = f)
	print
	if save:
		return P, RT, np.array(D).mean(), RP, AP, np.array(mBc).mean(), np.array(ABC).mean(), len(NoMove)/float(n_trials)
	return histor, P

if __name__ == "__main__":

	reset(protocol = 'Piron')
	hist, P = learning_trials(hist = True)
	#if 1: display_ctx(hist, 3.0)
