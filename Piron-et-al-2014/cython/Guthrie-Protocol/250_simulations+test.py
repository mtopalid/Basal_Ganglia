import numpy as np
import os
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Piron-et-al-2014/cython/')
from model import *
from learning import *
from testing import *
from parameters import *



if __name__ == "__main__":

	path = 'Results+test'#
	if not os.path.exists(path):
		os.makedirs(path)
	debugging = path + '/Debugging.txt'#.txt'
	f = open(debugging, 'wb')


	CVtotal = np.zeros((simulations, n))
	WtotalSTR = np.zeros((simulations, n))
	WtotalCog = np.zeros((simulations, n))
	WtotalMot = np.zeros((simulations, n))

	P = np.zeros((simulations, n_trials))
	RT = np.zeros((simulations, n_trials))
	D = np.zeros(simulations)
	RP = np.zeros((simulations, n))
	AP = np.zeros((simulations, n))
	mBc = np.zeros(simulations)
	ABC = np.zeros(simulations)
	NoMove = np.zeros(simulations)

	P_test = np.zeros((simulations, n_trials))
	RT_test = np.zeros((simulations, n_trials))
	AP_test = np.zeros((simulations, n))
	D_test = np.zeros(simulations)
	mBc_test = np.zeros(simulations)
	ABC_test = np.zeros(simulations)
	NoMove_test = np.zeros(simulations)

	for i in range(simulations):
		print 'Experiment: ', i + 1
		reset(protocol = 'Guthrie')
		p,r,d,mbc,abc,nomove,rt = [], [], [], [], [], [], []
		rp = np.zeros(n)
		ap = np.zeros(n)
		p_test,r_test,d_test,mbc_test,abc_test,nomove_test,rt_test = [], [], [], [], [], [], []
		rp_test = np.zeros(n)
		ap_test = np.zeros(n)
		for j in range(n_trials):

			connections["GPI.cog -> THL.cog"].active = True
			connections["GPI.mot -> THL.mot"].active = True
			rt, p, d, rp, ap, mbc, abc, nomove = learning(f = f, trial_n = j, debugging = False, protocol = 'Guthrie', learn = True, hist = False, P = p, D = d, mBc = mbc, ABC = abc, NoMove = nomove, RT = rt, RP = rp, AP = ap)

			W_COG = connections["CTX.cog -> CTX.ass"].weights
			W_MOT= connections["CTX.mot -> CTX.ass"].weights
			W_STR = connections["CTX.cog -> STR.cog"].weights

			connections["GPI.cog -> THL.cog"].active = False
			connections["GPI.mot -> THL.mot"].active = False
			rt_test, p_test, d_test, rp_test, ap_test, mbc_test, abc_test, nomove_test = learning(f = f, trial_n = j, debugging = False, protocol = 'Guthrie', learn = False, hist = False, P = p_test, D = d_test, mBc = mbc_test, ABC = abc_test, NoMove = nomove_test, RT = rt_test, AP = ap_test)
		print '\nLearning Phase\n'
		debug(f = f, P = p, D = d, mBc = mbc, ABC = abc, NoMove = nomove, RT = rt, RP = rp, AP = ap)
		debug_learning(connections["CTX.cog -> CTX.ass"].weights, connections["CTX.mot -> CTX.ass"].weights, connections["CTX.cog -> STR.cog"].weights, cues_value = CUE["value"], f = f)
		print '\n\nTesting Phase\n'
		debug(f = f, P = p_test, D = d_test, mBc = mbc_test, ABC = abc_test, NoMove = nomove_test, RT = rt_test, AP = ap_test)
		debug_learning(connections["CTX.cog -> CTX.ass"].weights, connections["CTX.mot -> CTX.ass"].weights, connections["CTX.cog -> STR.cog"].weights, cues_value = CUE["value"], f = f)
		print
		print
		P[i,:] 		= p
		RT[i,:]		= rt
		D[i] 		= np.array(d).mean()
		RP[i,:]		= rp
		AP[i,:]		= ap
		mBc[i]		= np.array(mbc).mean()
		ABC[i]		= np.array(abc).mean()
		NoMove[i]	= len(nomove)/float(n_trials)
		P_test[i,:] 	= p_test
		RT_test[i,:]	= rt_test
		D_test[i] 		= np.array(d_test).mean()
		AP_test[i,:]	= ap_test
		mBc_test[i]		= np.array(mbc_test).mean()
		ABC_test[i]		= np.array(abc_test).mean()
		NoMove_test[i]	= len(nomove_test)/float(n_trials)
		CVtotal[i, :] = CUE["value"]
		WtotalSTR[i,:] = connections["CTX.cog -> STR.cog"].weights
		WtotalCog[i,:] = connections["CTX.cog -> CTX.ass"].weights
		WtotalMot[i,:] = connections["CTX.mot -> CTX.ass"].weights
		print
		print
	print 'Learning\n'
	debug_total(f, P, D, ABC, NoMove, AP, RP, CVtotal, WtotalSTR, WtotalCog, WtotalMot)
	print '\n\nTesting\n'
	debug_total(f, P_test, D_test, ABC_test, NoMove_test, AP_test)

	f.close()

	file = path + '/MeanCuesValues.npy'
	np.save(file,CVtotal)
	file = path + '/Weights_Str.npy'
	np.save(file,WtotalSTR)
	file = path + '/Weights_Cog.npy'
	np.save(file,WtotalCog)
	file = path + '/Weights_Mot.npy'
	np.save(file,WtotalMot)

	file = path + '/NoMove.npy'
	np.save(file,NoMove)
	file = path + '/RT.npy'
	np.save(file,RT)
	file = path + '/Performance.npy'
	np.save(file,P)
	file = path + '/DifferentChoices.npy'
	np.save(file,D)
	file = path + '/MotBefCog.npy'
	np.save(file,mBc)
	file = path + '/ActBefCues.npy'
	np.save(file,ABC)

	file = path + '/NoMove-test.npy'
	np.save(file,NoMove_test)
	file = path + '/RT-test.npy'
	np.save(file,RT_test)
	file = path + '/Performance-test.npy'
	np.save(file,P_test)
	file = path + '/DifferentChoices-test.npy'
	np.save(file,D_test)
	file = path + '/MotBefCog-test.npy'
	np.save(file,mBc_test)
	file = path + '/ActBefCues-test.npy'
	np.save(file,ABC_test)
