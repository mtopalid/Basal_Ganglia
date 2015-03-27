import numpy as np
import random
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')
from model import *
from display import *
from trial import *
from learning import *
from testing import *

if __name__ == "__main__":

	reset(protocol = 'Piron')
	print 'Learning Phase'
	learning_trials(trials = 60, debugging = False, protocol = 'Piron', familiar = True)
	connections["GPI.cog -> THL.cog"].active = False
	connections["GPI.mot -> THL.mot"].active = False
	print 'Testing Familiar without GPi'
	hist = testing_trials(trials = 60, debugging = False)
	print 'Testing UnFamiliar without GPi'
	hist = testing_trials(trials = 60, debugging = False, protocol = 'Piron', familiar = False)
	#if 1: display_ctx(hist, 3.0)
	connections["GPI.cog -> THL.cog"].active = True
	connections["GPI.mot -> THL.mot"].active = True

	W_COG = connections["CTX.cog -> CTX.ass"].weights
	W_MOT= connections["CTX.mot -> CTX.ass"].weights
	W_STR = connections["CTX.cog -> STR.cog"].weights
	print 'Testing UnFamiliar'
	learning_trials(trials = 60, debugging = False, protocol = 'Piron', familiar = False, W_COG = W_COG, W_MOT = W_MOT, W_STR = W_STR)
	W_COG = connections["CTX.cog -> CTX.ass"].weights
	W_MOT= connections["CTX.mot -> CTX.ass"].weights
	W_STR = connections["CTX.cog -> STR.cog"].weights
	print 'Testing Familiar'
	learning_trials(trials = 60, debugging = False, protocol = 'Piron', W_COG = W_COG, W_MOT = W_MOT, W_STR = W_STR)
	#if 1: display_ctx(hist, 3.0)
