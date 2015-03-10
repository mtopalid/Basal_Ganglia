import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Piron-et-al-2014/cython/')
from model import *
from display import *
from learning import *

if __name__ == "__main__":
	print 'test'
	reset(protocol = 'Guthrie')
	hist, P = learning_trials(hist = True, protocol = 'Guthrie')
	#if 1: display_ctx(hist, 3.0)
