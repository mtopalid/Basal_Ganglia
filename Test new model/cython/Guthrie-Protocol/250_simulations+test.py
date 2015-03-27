import numpy as np
import os
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Test new model/cython/')
from model import *
from learning import *
from testing import *
from parameters import *



if __name__ == "__main__":

	path = 'Results+test'#-HalfParam
	if not os.path.exists(path):
		os.makedirs(path)
	if 0:
		debugging = path + '/Debugging.txt'#.txt'
		f = open(debugging, 'wb')
		folder = 'Results'#-HalfParam
		file = folder + '/Weights_Cog.npy'
		cog = np.load(file)[-1,-1]
		file = folder + '/Weights_Mot.npy'
		mot = np.load(file)[-1,-1]
		file = folder + '/Weights_Str.npy'
		str = np.load(file)[-1,-1]
	RT = np.zeros((simulations, n_trials))
	RT_test = np.zeros((simulations, n_trials))
	RT_test_bg = np.zeros((simulations, n_trials))
	RT_test_ctx = np.zeros((simulations, n_trials))
	for i in range(simulations):
		print 'Experiment: ', i + 1
		reset(protocol = 'Guthrie')
		initWcog = connections["CTX.cog -> CTX.ass"].weights
		initWmot = connections["CTX.mot -> CTX.ass"].weights
		initWdstr = connections["CTX.cog -> dSTR.cog"].weights
		initWistr = connections["CTX.cog -> iSTR.cog"].weights
		if 0:
			connections["CTX.cog -> CTX.ass"].weights = cog
			connections["CTX.mot -> CTX.ass"].weights = mot
			connections["CTX.cog -> STR.cog"].weights = str
		p,r,d,mbc,abc,nomove,rt = [], [], [], [], [], [], []
		rp = np.zeros(n)
		ap = np.zeros(n)
		p_test,r_test,d_test,mbc_test,abc_test,nomove_test,rt_test = [], [], [], [], [], [], []
		rp_test = np.zeros(n)
		ap_test = np.zeros(n)
		p_test_ctx,r_test_ctx,d_test_ctx,mbc_test_ctx,abc_test_ctx,nomove_test_ctx,rt_test_ctx = [], [], [], [], [], [], []
		rp_test_ctx = np.zeros(n)
		ap_test_ctx = np.zeros(n)
		p_test_bg,r_test_bg,d_test_bg,mbc_test_bg,abc_test_bg,nomove_test_bg,rt_test_bg = [], [], [], [], [], [], []
		rp_test_bg = np.zeros(n)
		ap_test_bg = np.zeros(n)
		for j in range(n_trials):
			#print 'Trial: ', j+1
			connections["GPI.cog -> THL.cog"].active = True
			connections["GPI.mot -> THL.mot"].active = True
			temp_cog = connections["CTX.cog -> CTX.ass"].weights
			temp_mot = connections["CTX.mot -> CTX.ass"].weights
			temp_dstr = connections["CTX.cog -> dSTR.cog"].weights
			temp_istr = connections["CTX.cog -> iSTR.cog"].weights

			rt, p, d, rp, ap, mbc, abc, nomove = learning(trial_n = j, debugging = False, protocol = 'Guthrie', learn = True, hist = False, P = p, D = d, mBc = mbc, ABC = abc, NoMove = nomove, RT = rt, RP = rp, AP = ap)

			connections["CTX.cog -> CTX.ass"].weights = initWcog
			connections["CTX.mot -> CTX.ass"].weights = initWmot
			rt_test_bg, p_test_bg, d_test_bg, rp_test_bg, ap_test_bg, mbc_test_bg, abc_test_bg, nomove_test_bg = learning(trial_n = j, debugging = False, protocol = 'Guthrie', learn = False, hist = False, P = p_test_bg, D = d_test_bg, mBc = mbc_test_bg, ABC = abc_test_bg, NoMove = nomove_test_bg, RT = rt_test_bg, AP = ap_test_bg)
			connections["CTX.cog -> CTX.ass"].weights = temp_cog
			connections["CTX.mot -> CTX.ass"].weights = temp_mot

			connections["CTX.cog -> dSTR.cog"].weights = initWdstr
			connections["CTX.cog -> iSTR.cog"].weights = initWistr
			rt_test_ctx, p_test_ctx, d_test_ctx, rp_test_ctx, ap_test_ctx, mbc_test_ctx, abc_test_ctx, nomove_test_ctx = learning(trial_n = j, debugging = False, protocol = 'Guthrie', learn = False, hist = False, P = p_test_ctx, D = d_test_ctx, mBc = mbc_test_ctx, ABC = abc_test_ctx, NoMove = nomove_test_ctx, RT = rt_test_ctx, AP = ap_test_ctx)
			connections["CTX.cog -> dSTR.cog"].weights = temp_dstr
			connections["CTX.cog -> iSTR.cog"].weights = temp_istr


			connections["GPI.cog -> THL.cog"].active = False
			connections["GPI.mot -> THL.mot"].active = False
			rt_test, p_test, d_test, rp_test, ap_test, mbc_test, abc_test, nomove_test = learning(trial_n = j, debugging = False, protocol = 'Guthrie', learn = False, hist = False, P = p_test, D = d_test, mBc = mbc_test, ABC = abc_test, NoMove = nomove_test, RT = rt_test, AP = ap_test)

		print '\nLearning Phase\n'
		debug(P = p, D = d, mBc = mbc, ABC = abc, NoMove = nomove, RT = rt, RP = rp, AP = ap)
		debug_learning(connections["CTX.cog -> CTX.ass"].weights, connections["CTX.mot -> CTX.ass"].weights, connections["CTX.cog -> dSTR.cog"].weights, connections["CTX.cog -> iSTR.cog"].weights, cues_value = CUE["value"])
		print '\n\nTesting Phase\n'
		debug(P = p_test, D = d_test, mBc = mbc_test, ABC = abc_test, NoMove = nomove_test, RT = rt_test, AP = ap_test)
		print '\n\nTesting Phase BG\n'
		debug(P = p_test_bg, D = d_test_bg, mBc = mbc_test_bg, ABC = abc_test_bg, NoMove = nomove_test_bg, RT = rt_test_bg, AP = ap_test_bg)
		print
		print
		RT[i,:]		= rt
		RT_test[i,:]	= rt_test
		RT_test_bg[i,:]	= rt_test_bg
		RT_test_ctx[i,:]	= rt_test_ctx
		print
		print

	file = path + '/RT.npy'
	np.save(file,RT)
	file = path + '/RT-test.npy'
	np.save(file,RT_test)
	file = path + '/RT-test-ctx.npy'
	np.save(file,RT_test_ctx)
	file = path + '/RT-test-bg.npy'
	np.save(file,RT_test_bg)
