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
from group_functions import *
from populations import *
from connectivity import *
from parameters import *
from debugging import *
import matplotlib.pyplot as plt
import os


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

@after(clock.tick)
def regi(t):
	global timesteps, cognitive, motor, associative
	timesteps, cognitive, motor, associative = register(t, Cortex_cog, Cortex_mot, Cortex_ass, Striatum_cog, Striatum_mot, Striatum_ass, STN_cog, STN_mot, GPe_cog, GPe_mot, GPi_cog, GPi_mot, Thalamus_cog, Thalamus_mot)

P, R, RT = [], [], []
learn = True
@after(clock.tick)
def check_4_decision(t):
    global c1, c2, m1, m2, learn

    mot_choice = np.argmax(Cortex_mot['U'])

    # Check if Motor took a decision
    if abs(Cortex_mot['U'].max() - Cortex_mot['U'].min()) > 40.0 :

		time = t-500 * millisecond
		RT.append(time)
		if mot_choice == m1:
			cgchoice = c1
		elif mot_choice == m2:
			cgchoice = c2

		if cgchoice == min(c1,c2):
			P.append(1)
		else:
			P.append(0)
		if learn and np.array(P[-15:]).mean() < 0.95:
			reward = learning(cues_reward, cues_value, Cortex_cog, Striatum_cog, W_str, W_cx_cog, cgchoice, mot_choice, W_cx_mot, Cortex_mot)
			R.append(reward)
			debug(cgchoice, c1, c2, P = P, R = R, time = time, reward = reward)
		else:
			debug(cgchoice, c1, c2, P = P, time = time)

		end()



# Run simulation
np.random.seed(123)
learning_trials = 40
testing_trials 	= 20
print "\nLearning Phase\n"
for i in range(learning_trials):

	print "Trial: ", i+1
	clock.reset()
	reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
	reset_register()
	run(time=duration, dt=dt)

debug_weights(W_cx_cog, W_cx_mot, W_str)

P, R, RT = [], [], []
print "\nHabitual condition without GPi\n"
for i in range(testing_trials):

	print "Trial: ", i+1
	if i==0:
		clock.reset()
		reset(network, Cortex_mot, Cortex_cog, Cortex_ass, GPic = GPic.weights, GPim = GPim.weights, change = True)
		reset_register()
		learn = False
		run(time=duration, dt=dt)
	else:
		clock.reset()
		reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
		reset_register()
		run(time=duration, dt=dt)
print "\nMean Response time	: %.3fms" % np.array(RT).mean()
print "Performance: 		", float(np.sum(P))/len(P)*100, "%\n"

P, R, RT = [], [], []
type = "unfamiliar"
print "\nNovelty condition without GPi\n"
for i in range(testing_trials):

	print "Trial: ", i+1
	clock.reset()
	reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
	reset_register()
	run(time=duration, dt=dt)
print "\nMean Response time	: %.3fms" % np.array(RT).mean()
print "Performance: 		", float(np.sum(P))/len(P)*100, "%\n"


P, R, RT = [], [], []
type = "familiar"
print "\nHabitual condition with GPi\n"
for i in range(testing_trials):

	print "Trial: ", i+1
	if i==0:
		clock.reset()
		reset(network, Cortex_mot, Cortex_cog, Cortex_ass, GPic = GPic.weights, GPim = GPim.weights, change = True, gpi = True)
		reset_register()
		learn = True
		run(time=duration, dt=dt)
	else:
		clock.reset()
		reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
		reset_register()
		run(time=duration, dt=dt)
print "\nMean Response time	: %.3fms" % np.array(RT).mean()
print "Performance: 		", float(np.sum(P))/len(P)*100, "%\n"


P, R, RT = [], [], []
type = "unfamiliar"
print "\nNovelty condition with GPi\n"
for i in range(testing_trials):

	print "Trial: ", i+1
	clock.reset()
	reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
	reset_register()
	run(time=duration, dt=dt)
print "\nMean Response time	: %.3fms" % np.array(RT).mean()
print "Performance: 		", float(np.sum(P))/len(P)*100, "%\n"

figure(timesteps, cognitive, motor)
