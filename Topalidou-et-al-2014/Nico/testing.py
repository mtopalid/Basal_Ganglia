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
from model import *
from display import *
from single_trial import *
from learning import *

def sigmoid(V,Vmin=Vmin,Vmax=Vmax,Vh=Vh,Vc=Vc):
    return  Vmin + (Vmax-Vmin)/(1.0+np.exp((Vh-V)/Vc))

def testing_trials(f = None, n_trials = n_trials, debugging = True, save = False):
	P, R, D, mBc, ABC, NoMove = [], [], [], [], [], [] # ABC: Activity before cues
	RP = np.zeros(4)
	AP = np.zeros(4)
	for j in range(n_trials):
		if debugging:
			print 'Trial: ', j + 1
		hist = single_trial(f = f, trial = j, learn = False, debugging = debugging, P = P, D = D, RP = RP, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
		if not len(P) == j+1:
			P.append(0)
	debug(f = f, P = P, D = D, AP = AP, mBc = mBc, ABC = ABC, NoMove = NoMove)
	print
	if save:
		return hist, P, np.array(D).mean(), AP, np.array(mBc).mean(), np.array(ABC).mean(), len(NoMove)/float(n_trials)
	return hist

if __name__ == "__main__":

	reset()
	hist = learning_trials(debugging = False)
	hist = testing_trials(debugging = False)
	if 1: display_ctx(hist, 3.0)
	connections["GPI.cog -> THL.cog"].active = False
	connections["GPI.mot -> THL.mot"].active = False
	hist = testing_trials(debugging = False)
	if 1: display_ctx(hist, 3.0)
