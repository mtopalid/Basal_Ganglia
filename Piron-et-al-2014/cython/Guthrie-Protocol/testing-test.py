import numpy as np
import random
import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Piron-et-al-2014/cython/')
from model import *
from display import *
from trial import *
from learning import *
from testing import *

if __name__ == "__main__":

	reset(protocol = 'Guthrie')
	print 'Learning Phase'
	learning_trials(trials = n_trials, debugging = False, protocol = 'Guthrie', familiar = True)
	print 'Testing Phase'
	histor = testing_trials(trials = n_trials, debugging = False, protocol = 'Guthrie')
	#if 1: display_ctx(hist, 3.0)
