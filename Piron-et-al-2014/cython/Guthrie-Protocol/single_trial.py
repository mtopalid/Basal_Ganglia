import sys
sys.path.append('/Users/mtopalid/Desktop/PhD/Models/Basal_Ganglia/Piron-et-al-2014/cython/')
from model import *
from display import *
from trial import *

reset(protocol = 'Guthrie')
#connections["CTX.cog -> STR.cog"].weights = np.array([ 0.75, 0.4761739, 0.45899682, 0.46005381])
histor, time = trial(hist = True, debugging = True, protocol = 'Guthrie')
if 1: display_ctx(histor, 3.0)
if 0: display_ctx(histor, 3.0, "single-trial.pdf")
if 0: display_all(histor, 3.0, "single-trial-all.pdf")
