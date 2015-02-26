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

start = 500*millisecond
# Trial setup
@clock.at(start)
def trials(t):
	global c1, c2, m1, m2, trial
	c1, c2, m1, m2 = set_trial(Cortex_mot, Cortex_cog, Cortex_ass, trial = trial)

@clock.at(2.5*second + start)
def rt_trial(t):
    reset_trial(Cortex_mot, Cortex_cog, Cortex_ass)

@after(clock.tick)
def regi(t):
	global timesteps, cognitive, motor, associative
	timesteps, cognitive, motor, associative = register(t, Cortex_cog, Cortex_mot, Cortex_ass, Striatum_cog, Striatum_mot, Striatum_ass, STN_cog, STN_mot, GPe_cog, GPe_mot, GPi_cog, GPi_mot, Thalamus_cog, Thalamus_mot)

cues_value = np.ones(4) * 0.5
cues_reward = np.array([3.,2.,1.,0.])/3
motch = 0
P, R, RT = [], [], []
learn = True
@after(clock.tick)
def check_4_decision(t):
    global c1, c2, m1, m2, learn, decision_time, motch
    ind = int(t*1000)
    timesteps[ind] = t
    motor[0,:,ind] = Cortex_mot['U'].ravel()
    cognitive[0,:,ind] = Cortex_cog['U'].ravel()

    mot_choice = np.argmax(Cortex_mot['U'])

    # Check if Motor took a decision
    if abs(Cortex_mot['U'].max() - Cortex_mot['U'].min()) > 40.0 and motch == 0:

		motch = 1
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
		if learn and np.array(P).mean()<0.95:
			reward = learning(cues_reward, cues_value, Cortex_cog, Striatum_cog, W_str, W_cx_cog, cgchoice, mot_choice, W_cx_mot, Cortex_mot)
			R.append(reward)
			debug(cgchoice, c1, c2, P = P, R = R, time = decision_time, reward = reward)
			debug_weights(W_cx_cog, W_cx_mot, W_str)
		#else:
			#debug(cgchoice, c1, c2, P = P, time = decision_time)

		#end()



# Run simulation
save = True
np.random.seed(123)
learning_trials = 180

cues_value = np.ones(4) * 0.5
P, R, RT = [], [], []

for trial in range(learning_trials):
	global trial
	print "Trial: ", trial+1
	clock.reset()
	reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
	run(time=duration, dt=dt)
	if not len(P) == trial+1:
		decision_time = duration - 500 * millisecond
		RT.append(decision_time)
		P.append(0)
	if np.mean(P) > .95:
		end()
	motch = 0
print "Performance: ", float(np.sum(P))/len(P)*100, "%"
debug_weights(W_cx_cog, W_cx_mot, W_str)

reset_register()
clock.reset()
reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
run(time=duration, dt=dt)

figure(timesteps, cognitive, motor)
plt.show()
