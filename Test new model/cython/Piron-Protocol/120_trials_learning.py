import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')
from model import *
from display import *
from learning import *

if __name__ == "__main__":
	print 'test'
	reset(protocol = 'Piron')
	hist, P = learning_trials(hist = True, protocol = 'Piron', trials = n_learning_trials)
	#if 1: display_ctx(hist, 3.0)
