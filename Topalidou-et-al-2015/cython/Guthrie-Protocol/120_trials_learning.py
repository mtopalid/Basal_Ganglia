import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Topalidou-et-al-2015/cython/')
from model import *
from display import *
from learning import *

if __name__ == "__main__":
	inverse = input('\nDo you want to have an inverse of Probabilities during the simulation?\nChoose 1 for True or 0 for False\n')
	if inverse:
		inverse_trial = input('\nAfter how many trials will be the inverse?\n')
		inverse_all = input('\nDo you want to inverse all probabilities or just the middle ones?\nChoose 1 for all or 0 for middle ones\n')
	else:
		inverse_trial = 0
		inverse_all = 0

	reset(protocol = 'Guthrie')
	hist, P = learning_trials(inversable = inverse, inverse_all = inverse_all, inverse_trial = inverse_trial, hist = True, protocol = 'Guthrie')
	if 1: display_ctx(hist, 3.0)
