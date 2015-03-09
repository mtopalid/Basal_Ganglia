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
import random
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2014/cython/')
from model import *
from display import *
from single_trial import *
from parameters import *


def learning_trials(f = None, n_trials = n_trials, debugging = True, save = False):
	P, R, D, mBc, ABC, NoMove = [], [], [], [], [], []
	RP = np.zeros(n)
	AP = np.zeros(n)
	for j in range(n_trials):
		if debugging:
			print 'Trial: ', j + 1
		hist = single_trial(f = f, trial = j, learn = True, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
		if not len(P) == j+1:
			P.append(0)
	debug(f = f, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	debug_learning(connections["CTX.cog -> CTX.ass"].weights, connections["CTX.mot -> CTX.ass"].weights, connections["CTX.cog -> STR.cog"].weights, cues_value = CUE["value"], f = f)
	print
	if save:
		return hist, P, np.array(D).mean(), RP, AP, np.array(mBc).mean(), np.array(ABC).mean(), len(NoMove)/float(n_trials)
	return hist

if __name__ == "__main__":

	reset()
	hist = learning_trials()
	if 1: display_ctx(hist, 3.0)

	hist = single_trial()
	mot_choice = np.argmax(CTX.mot.U)
	cog_choice = np.argmax(CTX.cog.U)

	for i in range(n):
		if mot_choice == CUE["mot"][:n][i]:
			choice = CUE["cog"][:n][i]
	debug(cgchoice = choice, c1 = CUE["cog"][:n][0], c2 = CUE["cog"][:n][1])

	if 1: display_ctx(hist, 3.0)
