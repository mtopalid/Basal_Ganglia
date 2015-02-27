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
	c1, c2, m1, m2 = set_trial(Cortex_mot, Cortex_cog, Cortex_ass, trial = 1)


@clock.at(2.5*second + start)
def rt_trial(t):
    reset_trial(Cortex_mot, Cortex_cog, Cortex_ass)


@after(clock.tick)
def regi(t):
	global timesteps, cognitive, motor, associative
	timesteps, cognitive, motor, associative = register(t, Cortex_cog, Cortex_mot, Cortex_ass, Striatum_cog, Striatum_mot, Striatum_ass, STN_cog, STN_mot, GPe_cog, GPe_mot, GPi_cog, GPi_mot, Thalamus_cog, Thalamus_mot)

motch = 0
@after(clock.tick)
def check_4_decision(t):
    global c1, c2, m1, m2, learn, decision_time, motch

    mot_choice = np.argmax(Cortex_mot['U'])

    # Check if Motor took a decision
    if abs(Cortex_mot['U'].max() - Cortex_mot['U'].min()) > 40.0 and motch == 0:

		motch = 1
		decision_time = t - 500 * millisecond
		if mot_choice == m1:
			cgchoice = c1
		elif mot_choice == m2:
			cgchoice = c2

		P = 1 if cgchoice == min(c1,c2) else 0

		debug(cgchoice, c1, c2, time = decision_time)
		print "Performance:		", P
		#end()



# Run trial
np.random.seed(123)
clock.reset()
reset(network, Cortex_mot, Cortex_cog, Cortex_ass)
run(time=duration, dt=dt)

figure(timesteps, cognitive, motor)
displayALL(timesteps, cognitive, motor, associative)
plt.show()
