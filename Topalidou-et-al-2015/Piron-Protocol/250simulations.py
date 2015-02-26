# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License.
#
# Contributors:
#  * Nicolas P. Rougier (Nicolas.Rougier@inria.fr)
#  * Meropi Topalidou (Meropi.Topalidou@inria.fr)
# -----------------------------------------------------------------------------

# Packages import
import sys
from dana import *
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015')
from trial import *
from display import *
from weights import *
from learning import *
from populations import *
from connectivity import *
from save import *
from parameters import *
from debugging import *
import matplotlib.pyplot as plt
import os
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015')
import parameters as p


Cortex_cog, Cortex_mot, Cortex_ass, Striatum_cog, Striatum_mot, Striatum_ass, STN_cog, STN_mot, GPe_cog, GPe_mot, GPi_cog, GPi_mot, Thalamus_cog, Thalamus_mot = populations()
W_str, W_cx_cog, W_cx_mot, GPic, GPim = connections(Cortex_cog, Cortex_mot, Cortex_ass, Striatum_cog, Striatum_mot, Striatum_ass, STN_cog, STN_mot, GPe_cog, GPe_mot, GPi_cog, GPi_mot, Thalamus_cog, Thalamus_mot)

type = "familiar"
start = 500*millisecond
# Trial setup
@clock.at(start)
def trial(t):
	global c1, c2, m1, m2, type
	c1, c2, m1, m2 = set_trial(Cortex_mot, Cortex_cog, Cortex_ass, type)

@clock.at(2.5*second + start)
def rt_trial(t):
    reset_trial(Cortex_mot, Cortex_cog, Cortex_ass)

cues_value = np.ones(4) * 0.5
cues_reward = np.array([0.75,0.25,0.75,0.25])

P, R, RT = [], [], []
learn = True
@after(clock.tick)
def register(t):
    global c1, c2, m1, m2, learn, decision_time

    mot_choice = np.argmax(Cortex_mot['U'])

    # Check if Motor took a decision
    if abs(Cortex_mot['U'].max() - Cortex_mot['U'].min()) > 40.0 :

		decision_time = t - 500 * millisecond
		RT.append(decision_time)
		if mot_choice == m1:
			cgchoice = c1
		elif mot_choice == m2:
			cgchoice = c2

		if cgchoice == min(c1,c2):
			P.append(1)
		else:
			P.append(0)
		if learn and np.array(P[-20:]).mean() < 0.95:
			reward = learning(cues_reward, cues_value, Cortex_cog, Striatum_cog, W_str, W_cx_cog, cgchoice, mot_choice, W_cx_mot, Cortex_mot)
			R.append(reward)
			#debug(cgchoice, c1, c2, P = P, R = R, time = decision_time, reward = reward)
		#else:
			#debug(cgchoice, c1, c2, P = P, time = decision_time)

		end()



# Run simulation
save = True
np.random.seed(123)
learning_trials = 80
testing_trials 	= 40
simulations = 2

LearningOptimumTrials = np.zeros((simulations,learning_trials))
RTmean_Fam_GPi,RTmean_UnFam_GPi,RTmean_Fam,RTmean_UnFam,Pmean_Fam_GPi,Pmean_UnFam_GPi,Pmean_Fam,Pmean_UnFam,P_Fam_GPi,P_UnFam_GPi,P_Fam,P_UnFam = initial_arrays2save(simulations, testing_trials)
for simulation in range(simulations):

	print "Simulation ", simulation + 1


	W_cx_cog.weights[np.where(W_cx_cog.weights !=0)] = Cx_cog_ass
	init_weights(W_cx_cog, Wmin = 0.9, Wmax = 1.0)
	W_cx_mot.weights[np.where(W_cx_mot.weights !=0)] = Cx_mot_ass
	init_weights(W_cx_mot, Wmin = 0.9, Wmax = 1.0)
	W_str.weights[np.where(W_str.weights !=0)] = Cx_Str_cog
	init_weights(W_str)
	cues_value = np.ones(4) * 0.5
	P, R, RT = [], [], []

	print "\nLearning Phase\n"
	type = "familiar"
	for i in range(learning_trials):

		#print "Trial: ", i+1
		clock.reset()
		reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
		run(time=duration, dt=dt)
		if not len(P) == i+1:
			decision_time = duration - 500 * millisecond
			RT.append(decision_time)
			P.append(0)

	print "Performance: ", float(np.sum(P))/len(P)*100, "%"
	debug_weights(W_cx_cog, W_cx_mot, W_str)

	LearningOptimumTrials[simulation,:] = P

	D = np.zeros(testing_trials)
	P, R, RT = [], [], []
	print "\nHabitual condition without GPi\n"
	for i in range(testing_trials):

		#print "Trial: ", i+1
		if i==0:
			clock.reset()
			reset(network, Cortex_mot, Cortex_cog, Cortex_ass, GPic = GPic.weights, GPim = GPim.weights, change = True)
			learn = False
			run(time=duration, dt=dt)
		else:
			clock.reset()
			reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
			run(time=duration, dt=dt)
		if not len(P) == i+1:
			decision_time = duration - 500 * millisecond
			RT.append(decision_time)
			P.append(0)
		D[i] = decision_time
	print "\nMean Response time	: %.3fms" % np.array(RT).mean()
	print "Performance: 		", float(np.sum(P))/len(P)*100, "%\n"
	RTmean_Fam[simulation,:], Pmean_Fam[simulation], P_Fam[simulation,:] = save_2_arrays(D, P)

	D = np.zeros(testing_trials)
	P, R, RT = [], [], []
	type = "unfamiliar"
	print "\nNovelty condition without GPi\n"
	for i in range(testing_trials):

		#print "Trial: ", i+1
		clock.reset()
		reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
		run(time=duration, dt=dt)
		if not len(P) == i+1:
			decision_time = duration - 500 * millisecond
			RT.append(decision_time)
			P.append(0)
		D[i] = decision_time
	print "\nMean Response time	: %.3fms" % np.array(RT).mean()
	print "Performance: 		", float(np.sum(P))/len(P)*100, "%\n"
	RTmean_UnFam[simulation,:], Pmean_UnFam[simulation], P_UnFam[simulation,:] = save_2_arrays(D, P)


	D = np.zeros(testing_trials)
	P, R, RT = [], [], []
	type = "familiar"
	print "\nHabitual condition with GPi\n"
	for i in range(testing_trials):

		#print "Trial: ", i+1
		if i==0:
			clock.reset()
			reset(network, Cortex_mot, Cortex_cog, Cortex_ass, GPic = GPic.weights, GPim = GPim.weights, change = True, gpi = True)
			learn = True
			run(time=duration, dt=dt)
		else:
			clock.reset()
			reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
			run(time=duration, dt=dt)
		if not len(P) == i+1:
			decision_time = duration - 500 * millisecond
			RT.append(decision_time)
			P.append(0)
		D[i] = decision_time
	print "\nMean Response time	: %.3fms" % np.array(RT).mean()
	print "Performance: 		", float(np.sum(P))/len(P)*100, "%\n"
	RTmean_Fam_GPi[simulation,:], Pmean_Fam_GPi[simulation], P_Fam_GPi[simulation,:] = save_2_arrays(D, P)


	D = np.zeros(testing_trials)
	P, R, RT = [], [], []
	type = "unfamiliar"
	print "\nNovelty condition with GPi\n"
	for i in range(testing_trials):

		#print "Trial: ", i+1
		clock.reset()
		reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
		run(time=duration, dt=dt)
		if not len(P) == i+1:
			decision_time = duration - 500 * millisecond
			RT.append(append)
			P.append(decision_time)
		D[i] = decision_time
	print "\nMean Response time	: %.3fms" % np.array(RT).mean()
	print "Performance: 		", float(np.sum(P))/len(P)*100, "%\n"
	RTmean_UnFam_GPi[simulation,:], Pmean_UnFam_GPi[simulation], P_UnFam_GPi[simulation,:] = save_2_arrays(D, P)

#figure(timesteps, cognitive, motor)
if save:
	save_in_files('Results', RTmean_Fam_GPi,RTmean_UnFam_GPi,RTmean_Fam,RTmean_UnFam,Pmean_Fam_GPi,Pmean_UnFam_GPi,Pmean_Fam,Pmean_UnFam,P_Fam_GPi,P_UnFam_GPi,P_Fam,P_UnFam,LearningOptimumTrials)
