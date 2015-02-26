from dana import *
import numpy as np
from parameters import *

def init_weights(L, gain=1, Wmin = Wmin, Wmax = Wmax):

    W = L._weights
    N = np.random.normal(0.5, 0.005, W.shape)
    N = np.minimum(np.maximum(N, 0.0),1.0)
    L._weights = gain*W*(Wmin + (Wmax - Wmin)*N)


def clip(V, Vmin, Vmax):
    return np.minimum(np.maximum(V, Vmin), Vmax)

def connections(Cortex_cog, Cortex_mot, Cortex_ass, Striatum_cog, Striatum_mot, Striatum_ass, STN_cog, STN_mot, GPe_cog, GPe_mot, GPi_cog, GPi_mot, Thalamus_cog, Thalamus_mot):


	W_str = DenseConnection( Cortex_cog('U'),   Striatum_cog('I'), Cx_Str_cog)
	init_weights(W_str)
	L = DenseConnection( Cortex_mot('U'),   Striatum_mot('I'), Cx_Str_mot)
	init_weights(L)
	L = DenseConnection( Cortex_ass('U'),   Striatum_ass('I'), Cx_Str_ass)
	init_weights(L)
	L = DenseConnection( Cortex_cog('U'),   Striatum_ass('I'), Cx_cog_Str_ass)
	init_weights(L)
	L = DenseConnection( Cortex_mot('U'),   Striatum_ass('I'), Cx_mot_Str_ass)
	init_weights(L)

	DenseConnection( Cortex_cog('U'),   STN_cog('I'),       Cx_STN_cog )
	DenseConnection( Cortex_mot('U'),   STN_mot('I'),       Cx_STN_mot )
	DenseConnection( Striatum_cog('U'), GPe_cog('I'),       Str_Gpe_cog)
	DenseConnection( Striatum_mot('U'), GPe_mot('I'),       Str_Gpe_mot )
	DenseConnection( Striatum_ass('U'), GPe_cog('I'),       Str_ass_Gpe_cog)
	DenseConnection( Striatum_ass('U'), GPe_mot('I'),       Str_ass_Gpe_mot)
	DenseConnection( Striatum_cog('U'), GPi_cog('I'),       Str_Gpi_cog)
	DenseConnection( Striatum_mot('U'), GPi_mot('I'),       Str_Gpi_mot )
	DenseConnection( Striatum_ass('U'), GPi_cog('I'),       Str_ass_Gpi_cog)
	DenseConnection( Striatum_ass('U'), GPi_mot('I'),       Str_ass_Gpi_mot)
	DenseConnection( STN_cog('U'),      GPi_cog('I'),       STN_Gpi_cog )
	DenseConnection( STN_mot('U'),      GPi_mot('I'),       STN_Gpi_mot )
	DenseConnection( GPe_cog('U'),      STN_cog('I'), 		Gpe_STN_cog )
	DenseConnection( GPe_mot('U'),      STN_mot('I'), 		Gpe_STN_mot )
	DenseConnection( Cortex_cog('U'),   Thalamus_cog('I'),  Cx_Th_cog )
	DenseConnection( Cortex_mot('U'),   Thalamus_mot('I'),  Cx_Th_mot )

	DenseConnection( Cortex_cog('U'), Cortex_cog('I'), Cx_cog_cog)
	DenseConnection( Cortex_mot('U'), Cortex_mot('I'), Cx_mot_mot)
	DenseConnection( Cortex_ass('U'), Cortex_ass('I'), Cx_ass_ass)
	DenseConnection( Cortex_ass('U'), Cortex_mot('I'), Cx_ass_mot)
	DenseConnection( Cortex_ass('U'), Cortex_cog('I'), Cx_ass_cog)
	W_cx_cog = DenseConnection( Cortex_cog('U'), Cortex_ass('I'), Cx_cog_ass)
	init_weights(W_cx_cog, Wmin = 0.90, Wmax = 1.10)

	DenseConnection( Thalamus_cog('U'), Cortex_cog('I'),    Th_Cx_cog)
	DenseConnection( Thalamus_mot('U'), Cortex_mot('I'),    Th_Cx_mot)
	GPic = DenseConnection( GPi_cog('U'),Thalamus_cog('I'), Gpi_Th_cog )
	GPim = DenseConnection( GPi_mot('U'), Thalamus_mot('I'), Gpi_Th_mot )

	W_cx_mot = DenseConnection( Cortex_mot('U'), Cortex_ass('I'), Cx_mot_ass)
	init_weights(W_cx_mot, Wmin = 0.90, Wmax = 1.10)
	return W_str, W_cx_cog, W_cx_mot, GPic, GPim

