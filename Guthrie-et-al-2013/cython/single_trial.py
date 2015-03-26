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
from parameters import *

# Make GPI lesion
# connections["GPI.cog -> THL.cog"].active = False
# connections["GPI.mot -> THL.mot"].active = False

def single_trial(f = None, learn = False, debugging = False, trial = 0, NoMove = [], RT = [], ct = [], cog_time = [], mBc = [], ABC = [], P = [], D = [], AP = np.zeros(n), R = [], RP = np.zeros(n)):

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
	set_trial(n=2, trial = trial)
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
			time = i-500
			choice = process(learning = learn, P = P, D = D, AP = AP, R = R, RP = RP)
			if debugging:
				debug(f = f, cgchoice = choice, c1 = CUE["cog"][:n][0], c2 = CUE["cog"][:n][1],P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
				if learn:
					debug_learning(connections["CTX.cog -> STR.cog"].weights, CUE["value"],f = f)
				print
			hist = history()
			return hist
	NoMove.append(trial)
	if debugging:
		print 'Trial Failed!'
		print 'NoMove trial: ', NoMove
	hist = history()
	return hist
if __name__ == "__main__":

	reset()
	#connections["CTX.cog -> STR.cog"].weights = np.array([ 0.75, 0.4761739, 0.45899682, 0.46005381])
	hist = single_trial()
	if 0: display_ctx(hist, 3.0)
	if 0: display_ctx(hist, 3.0, "single-trial.pdf")
	if 1: display_all(hist, 3.0)#, "single-trial-all.pdf")
