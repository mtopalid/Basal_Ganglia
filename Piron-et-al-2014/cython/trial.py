import numpy as np
from model import *
from display import *
from parameters import *

# Make GPI lesion
# connections["GPI.cog -> THL.cog"].active = False
# connections["GPI.mot -> THL.mot"].active = False
def trial(hist = False, f = None, learn = False, debugging = False, trial_n = 0, protocol = 'Piron', familiar = True, NoMove = [], ct = [], cog_time = [], mBc = [], ABC = [], P = [], D = [], AP = np.zeros(n), RP = np.zeros(n)):

	reset_activities()
	reset_history()
	ct = None
	cog_time = None
	for i in xrange(  0, 500):
		iterate(dt)
		if CTX.cog.delta > 20 and not ct  and ABC :
			ABC.append(1)
			ct = 1
		if CTX.cog.delta > threshold and not cog_time:
			cog_time=i-500
	if not ct and ABC:
		ABC.append(0)
	set_trial(n=2, trial = trial_n, protocol = protocol, familiar = familiar)
	for i in xrange(500,3000):
		iterate(dt)

		# Test if a decision has been made
		if CTX.cog.delta > threshold and not cog_time:
			cog_time=i-500
		if CTX.mot.delta > decision_threshold:
			if not cog_time:
				mBc.append(1)
			else:
				mBc.append(0)
			time = (i-500)
			choice = process(learning = learn, P = P, D = D, AP = AP, RP = RP)
			if debugging:
				debug(f = f, RT = time, cgchoice = choice, c1 = CUE["cog"][:n][0], c2 = CUE["cog"][:n][1],P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
				if learn:
					debug_learning(connections["CTX.cog -> CTX.ass"].weights, connections["CTX.mot -> CTX.ass"].weights, connections["CTX.cog -> STR.cog"].weights, CUE["value"],f = f)
				print
				if hist:
					histor = history()
					return histor, time
			return time
	NoMove.append(trial)
	time = 2500
	if debugging:
		print 'Trial Failed!'
		print 'NoMove trial: ', NoMove
	if hist:
		histor = history()
		return histor, time
	else:
		return time
