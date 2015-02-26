import numpy as np
from parameters import *

choices  = np.array([[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]])
cues_cog = choices.repeat(30, axis = 0)
np.random.shuffle(cues_cog)
cues_mot = np.array([0,1,2,3])

def set_trial(Cortex_mot, Cortex_cog, Cortex_ass, type= "familiar", trial = None):

    if trial is not None:
		temp = np.array(cues_cog[trial,:])
		np.random.shuffle(temp)
		c1,c2 = temp
		np.random.shuffle(cues_mot)
		m1,m2 = cues_mot[:2]

    else:
		if type == "familiar":
			temp = np.array([0,1])
			np.random.shuffle(temp)
			c1, c2 = temp
			np.random.shuffle(temp)
			m1, m2 = temp
		elif type == "unfamiliar":
			temp = np.array([2,3])
			np.random.shuffle(temp)
			c1, c2 = temp
			np.random.shuffle(temp)
			m1, m2 = temp
    Cortex_mot['Iext'] = 0
    Cortex_cog['Iext'] = 0
    Cortex_ass['Iext'] = 0

    v = 7
    noise = 0.001
    Cortex_mot['Iext'][0,m1]  = v + np.random.normal(0,v*noise)
    Cortex_mot['Iext'][0,m2]  = v + np.random.normal(0,v*noise)
    Cortex_cog['Iext'][c1,0]  = v + np.random.normal(0,v*noise)
    Cortex_cog['Iext'][c2,0]  = v + np.random.normal(0,v*noise)
    Cortex_ass['Iext'][c1,m1] = v + np.random.normal(0,v*noise)
    Cortex_ass['Iext'][c2,m2] = v + np.random.normal(0,v*noise)

    return c1, c2, m1, m2

def reset_trial(Cortex_mot, Cortex_cog, Cortex_ass):

    Cortex_mot['Iext'] = 0
    Cortex_cog['Iext'] = 0
    Cortex_ass['Iext'] = 0

def reset(network, Cortex_mot, Cortex_cog, Cortex_ass, GPic = [], GPim = [], change = False, gpi = False):

    for group in network.__default_network__._groups:
        group['U'] = 0
        group['V'] = 0
        group['I'] = 0
    reset_trial(Cortex_mot, Cortex_cog, Cortex_ass)
    if change:
		if gpi:
			for j in range(n):
				GPic[j,j] = -0.5
				GPim[j,j] = -0.5
		else:
			GPic[:] = 0
			GPim[:] = 0

timesteps   = np.zeros(size)
motor       = np.zeros((6, n, size))
cognitive   = np.zeros((6, n, size))
associative   = np.zeros((2, n * n, size))

def reset_register():
	global timesteps, cognitive, motor, associative
	timesteps   = np.zeros(size)
	motor       = np.zeros((6, n, size))
	cognitive   = np.zeros((6, n, size))
	associative   = np.zeros((2, n * n, size))

def register(t, Cortex_cog, Cortex_mot, Cortex_ass, Striatum_cog, Striatum_mot, Striatum_ass, STN_cog, STN_mot, GPe_cog, GPe_mot, GPi_cog, GPi_mot, Thalamus_cog, Thalamus_mot):
    ind = int(t*1000)
    timesteps[ind] = t

    cognitive[0,:,ind] = 	Cortex_cog['U'].ravel()
    motor[0,:,ind] = 		Cortex_mot['U'].ravel()
    associative[0,:,ind] = 	Cortex_ass['U'].ravel()

    cognitive[1,:,ind] = 	Striatum_cog['U'].ravel()
    motor[1,:,ind] = 		Striatum_mot['U'].ravel()
    associative[1,:,ind] = 	Striatum_ass['U'].ravel()

    cognitive[2,:,ind] = 	STN_cog['U'].ravel()
    motor[2,:,ind] = 		STN_mot['U'].ravel()

    cognitive[3,:,ind] = 	GPe_cog['U'].ravel()
    motor[3,:,ind] = 		GPe_mot['U'].ravel()

    cognitive[4,:,ind] = 	GPi_cog['U'].ravel()
    motor[4,:,ind] = 		GPi_mot['U'].ravel()

    cognitive[5,:,ind] = 	Thalamus_cog['U'].ravel()
    motor[5,:,ind] = 		Thalamus_mot['U'].ravel()

    return timesteps, cognitive, motor, associative

