import numpy as np

choices  = np.array([[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]])
cues_cog = choices.repeat(30, axis = 0)
np.random.shuffle(cues_cog)
cues_mot = np.array([0,1,2,3])

def set_trial(Cortex_mot, Cortex_cog, Cortex_ass, trial = None):

    if trial is not None:
		temp = np.array(cues_cog[trial,:])
    	np.random.shuffle(temp)
		c1,c2 = temp
    else:
		temp = np.array([0,1])
		np.random.shuffle(temp)
		c1, c2 = temp
	np.random.shuffle(cues_mot)
	m1,m2 = cues_mot
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
