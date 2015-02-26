import numpy as np
from weights import *
from parameters import *
from connectivity import *

# Learning parameters
decision_threshold = 40
alpha_c     = 0.05
alpha_LTP  	= 0.002
alpha_LTD  	= 0.001
Wmin, Wmax 	= 0.25, 0.75

def learning(cues_reward, cues_value, Cortex_cog, Striatum_cog, W_str, W_cx_cog, cgchoice, mot_choice, W_cx_mot, Cortex_mot):
	#Striatal Learning
	# Compute reward
	reward = float(np.random.uniform(0,1) < cues_reward[cgchoice])

	# Compute prediction error
	error = reward - cues_value[cgchoice]

	# Update cues values
	cues_value[cgchoice] += error* alpha_c

	# Learn
	lrate = alpha_LTP if error > 0 else alpha_LTD

	dw = error * lrate * Striatum_cog['U'][cgchoice][0]

	w = clip(W_str.weights[cgchoice, cgchoice] + dw, Wmin, Wmax)
	W_str.weights[cgchoice,cgchoice] = w

	wcx_cog = 0.01*alpha_LTP * np.ones(n) * np.minimum(Cortex_cog['U'][cgchoice][0],1.0)
	W_cx_cog.weights[cgchoice*n:(cgchoice + 1) * n,cgchoice] += wcx_cog

	wcx_mot = 0.01*alpha_LTP * np.minimum(Cortex_mot['U'][0][mot_choice],0.5)
	for i in range(n):
		W_cx_mot.weights[mot_choice*n + i, i] += wcx_mot

	return reward



	# Cortical Learning
	#y = W_cx.weights[cgchoice*4:(cgchoice + 1) * 4][cgchoice].reshape((1,4)) * Cortex_ass['U'][cgchoice].reshape((1,4))
	#dw_Cortex = 0.0001 * ndot(y, Cortex_ass['U'][cgchoice])
	#w = clip(W_cx.weights[cgchoice*4:(cgchoice + 1) * 4][cgchoice] + dw_Cortex, 0.095, 0.105)
	#W_cx.weights[cgchoice*4:(cgchoice + 1) * 4][cgchoice] = w
