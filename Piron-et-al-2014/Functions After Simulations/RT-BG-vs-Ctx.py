import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Piron-et-al-2014/cython/')

from parameters import *

def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c
protocol = input('Choose 1 for Guthrie-Protocol or 2 for Piron-Protocol\n')
if protocol == 1:
	folder = '../cython/Guthrie-Protocol/Results+test-HalfParam'#-HalfParam
	file = folder + '/RT.npy'
	load = np.load(file)
	MeanRT = load.mean(axis = 0)
	file = folder + '/RT-test.npy'
	load = np.load(file)
	MeanRTtest = load.mean(axis = 0)

	#file = folder+ '/MeanPerformance.npy'
	#np.save(file, MeanPerformance)

	fig = plt.figure()
	plt.plot(MeanRT, c = 'b', label = 'RT BG+Ctx')
	plt.plot(MeanRTtest, c = 'r', label = 'RT Ctx')
	plt.legend()

	plt.ylabel("Response Time (ms)")
	plt.xlabel("Trial number")
	plt.title("Piron model")
	#plt.ylim(0.495,0.51)
	file = folder + "/RT-BG-vs-Ctx.png"
	fig.savefig(file)
	plt.show()

elif protocol == 2:
	folder = '../cython/Piron-Protocol/Results'#
	#path = 'Piron-Protocol/Results-HalfLearningPar'
	file = folder + '/Performance-fam.npy'
	load = np.load(file)
	MeanPerformance = load.mean(axis = 0)
	C1 =  MeanPerformance.copy()
	file = folder + '/MeanPerformance-fam.npy'
	np.save(file, MeanPerformance)

	file = folder + '/Performance-unfam.npy'
	load = np.load(file)
	MeanPerformance = load.mean(axis = 0)
	C3 =  MeanPerformance.copy()
	file = folder+ '/MeanPerformance-unfam.npy'
	np.save(file, MeanPerformance)

	file = folder + '/Performance-fam_NoGPi.npy'
	load = np.load(file)
	load = np.delete(load, delete,0)
	MeanPerformance = load.mean(axis = 0)
	C2 =  MeanPerformance.copy()
	file = folder+ '/MeanPerformance-fam_NoGPi.npy'
	np.save(file, MeanPerformance)

	file = folder + '/Performance-unfam_NoGPi.npy'
	load = np.load(file)
	MeanPerformance = load.mean(axis = 0)
	C4 =  MeanPerformance.copy()
	file = folder+ '/MeanPerformance-unfam_NoGPi.npy'
	np.save(file, MeanPerformance)

	from matplotlib import rcParams
	rcParams['xtick.direction'] = 'out'
	rcParams['ytick.direction'] = 'out'

	plt.figure(figsize=(10,5), dpi=72, facecolor="white")
	axes = plt.subplot(111)
	axes.spines['right'].set_color('none')
	axes.spines['top'].set_color('none')
	axes.xaxis.set_ticks_position('bottom')
	axes.spines['bottom'].set_position(('data',0))
	axes.yaxis.set_ticks_position('left')

	n = len(C1)

	axes.plot(np.arange(n), C1,
			  lw=1.5, c='0.5', linestyle="--", label="HC with GPi")
	axes.plot(np.arange(n), C3,
			  lw=1.5, c='0.0', linestyle="--", label="NC with GPi")
	axes.plot(np.arange(n), C2,
			  lw=1.5, c='0.5', linestyle="-", label="HC without GPi")
	axes.plot(np.arange(n), C4,
			  lw=1.5, c='0.0', linestyle="-", label="NC without GPi")

	plt.legend(loc='lower right', frameon=False)

	plt.xlabel("Trial number")
	plt.ylabel("Proportion of optimum trials")

	plt.xlim(0,n)
	plt.ylim(0,1.05)
	plt.tight_layout()
	plt.savefig(folder + "/Performances.pdf")
	plt.show()


	C1 = np.load(folder + "/RT-fam.npy")
	C2 = np.load(folder + "/RT-fam_NoGPi.npy")
	C3 = np.load(folder + "/RT-unfam.npy")
	C4 = np.load(folder + "/RT-unfam_NoGPi.npy")

	fig = plt.figure(figsize=(6,5), dpi=72, facecolor="white")
	fig.subplots_adjust(bottom=0.25)
	fig.subplots_adjust(left=0.15)

	ax = plt.subplot(111)
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.yaxis.set_ticks_position('left')

	means = [np.mean(C1), np.mean(C3), np.mean(C2), np.mean(C4)]
	stds  = [ np.std(C1),  np.std(C3),  np.std(C2),  np.std(C4)]

	indices = 0.25+np.arange(4)
	width=0.75
	p1 = plt.bar(indices, means, width=width,  yerr=stds,
				 color=["1.", ".5", "1.", ".5"], edgecolor='k', ecolor='k')
	plt.xticks(indices+width/2., ('HC', 'NC', 'HC', 'NC') )

	# def label(i,j,text,X,Y):
	#     x = (X[i]+X[j])/2
	#     y = 1.25*max(Y[i], Y[j])
	#     dx = abs(X[i]-X[j])
	#     props = {'connectionstyle':'bar','arrowstyle':'-', 'shrinkA':20,'shrinkB':20,'lw':1}
	#     ax.annotate(text, xy=(x,y+100), zorder=10, fontsize=20, ha="center")
	#     ax.annotate('', xy=(X[i],y), xytext=(X[j],y), arrowprops=props)
	# label(0,1,"***", indices+width/2, means+stds)
	# label(1,2,"***", indices+width/2, means+stds)
	# label(2,3,"***", indices+width/2, means+stds)

	plt.ylabel("Reaction time (ms)", fontsize=16)
	plt.xlim(0,4.25)
	#plt.ylim(0,1200)
	#plt.tight_layout()

	b = 0.025

	plt.axhline(-325, b,.5-b, clip_on=False, color="k")
	ax.text(1.125,-350,"With GPi", clip_on=False, ha="center", va="top", fontsize=18)

	plt.axhline(-325, .5+b,1-b, clip_on=False, color="k")
	ax.text(3.125,-350,"Without GPi", clip_on=False, ha="center", va="top", fontsize=18)

	plt.savefig(folder + "/RT.pdf")
	plt.show()

