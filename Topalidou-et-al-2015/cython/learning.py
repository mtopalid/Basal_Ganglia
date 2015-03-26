import numpy as np
import random
from trial import *
from parameters import *

def learning(inverse = False, inverse_all = True, f = None, trial_n = 0, debugging = True, protocol = 'Piron', familiar = True, learn = True, hist = False, P = [], D = [], mBc = [], ABC = [], NoMove = [], RT = [], RP = None, AP = None):
	if hist:
		histor, time = trial(inverse = inverse, inverse_all = inverse_all, f = f, trial_n = trial_n, learn = learn, protocol = protocol, hist = hist, familiar = familiar, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	else:
		time = trial(inverse = inverse, inverse_all = inverse_all, f = f, trial_n = trial_n, learn = learn, protocol = protocol, hist = hist, familiar = familiar, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	RT.append(time)
	if not len(P) == trial_n+1:
		P.append(0)
	if hist:
		return histor, RT, P, D, RP, AP, mBc, ABC, NoMove
	else:
		return RT, P, D, RP, AP, mBc, ABC, NoMove

def learning_trials(inverse = False, inverse_all = True, inverse_trial = 50, f = None, hist = False, trials = n_trials, debugging = True, save = False, protocol = 'Piron', familiar = True, type = 'learning', W_COG = None, W_MOT = None, W_STR = None):
	trained = False
	while not trained:
		P, D, mBc, ABC, NoMove, RT = [], [], [], [], [], []
		RP = np.zeros(n)
		AP = np.zeros(n)
		wCog = np.zeros((trials,n))
		wMot = np.zeros((trials,n))
		wStr = np.zeros((trials,n))
		reset(protocol = protocol, W_COG = W_COG, W_MOT = W_MOT, W_STR = W_STR)
		for j in range(20):

			if debugging:
				print 'Trial: ', j + 1
			if hist:
				histor, RT, P, D, RP, AP, mBc, ABC, NoMove = learning(inverse = inverse, inverse_all = inverse_all, f = f, trial_n = j, debugging = debugging, protocol = protocol, familiar = familiar, hist = hist, P = P, D = D, mBc = mBc, ABC = ABC, NoMove = NoMove, RT = RT, RP = RP, AP = AP)
			else:
				RT, P, D, RP, AP, mBc, ABC, NoMove = learning(inverse = inverse, inverse_all = inverse_all, f = f, trial_n = j, debugging = debugging, protocol = protocol, familiar = familiar, hist = hist, P = P, D = D, mBc = mBc, ABC = ABC, NoMove = NoMove, RT = RT, RP = RP, AP = AP)

			wCog[j,:] = connections["CTX.cog -> CTX.ass"].weights
			wMot[j,:] = connections["CTX.mot -> CTX.ass"].weights
			wStr[j,:] = connections["CTX.cog -> STR.cog"].weights

		if type == 'learning':
			if np.mean(P) > 0.70:
				trained = True
		else:
			trained = True
	else:
		for i in range(j+1, trials):

			if inverse:
				if i == inverse_trial:
					CUE["reward"] = rewards_Guthrie_inverse
					inverse = True
			if debugging:
				print 'Trial: ', i + 1
			if hist:
				histor, RT, P, D, RP, AP, mBc, ABC, NoMove = learning(inverse = inverse, f = f, trial_n = i, debugging = debugging, protocol = protocol, familiar = familiar, hist = hist, P = P, D = D, mBc = mBc, ABC = ABC, NoMove = NoMove, RT = RT, RP = RP, AP = AP)
			else:
				RT, P, D, RP, AP, mBc, ABC, NoMove = learning(inverse = inverse, f = f, trial_n = i, debugging = debugging, protocol = protocol, familiar = familiar, hist = hist, P = P, D = D, mBc = mBc, ABC = ABC, NoMove = NoMove, RT = RT, RP = RP, AP = AP)
			wCog[i,:] = connections["CTX.cog -> CTX.ass"].weights
			wMot[i,:] = connections["CTX.mot -> CTX.ass"].weights
			wStr[i,:] = connections["CTX.cog -> STR.cog"].weights
	debug(inverse = inverse, f = f, RT = RT, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	debug_learning(connections["CTX.cog -> CTX.ass"].weights, connections["CTX.mot -> CTX.ass"].weights, connections["CTX.cog -> STR.cog"].weights, cues_value = CUE["value"], f = f)
	if save:
		return P, RT, np.array(D).mean(), RP, AP, np.array(mBc).mean(), np.array(ABC).mean(), len(NoMove)/float(n_trials), wCog, wMot, wStr
	if hist:
		return histor, P
	else:
		return P
