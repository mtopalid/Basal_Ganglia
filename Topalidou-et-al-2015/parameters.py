import numpy as np
import os
from dana import *
# Population size
n = 4

# Trial duration
duration = 3.0*second

# Default Time resolution
dt = 1.0*millisecond

# Size of vectors
size = int(duration/dt)

# Threshold
# -------------------------------------
Cortex_h   =  	-3.0
Striatum_h =   	0.0
STN_h      = 	-10.0
GPe_h      =  	-10.0
GPi_h      =  	10.0
Thalamus_h = 	-40.0

# Time constants
# -------------------------------------
tau = 0.01
Cortex_tau   = tau #0.01#tau #
Striatum_tau = tau #0.01
STN_tau      = tau #0.01
GPe_tau      = tau #0.01
GPi_tau      = tau #0.01
Thalamus_tau = tau #0.01
# Noise leve (%)
# -------------------------------------
Cortex_N   =   0.01
Striatum_N =   0.001
STN_N      =   0.001
GPe_N      =   0.001
GPi_N      =   0.001
Thalamus_N =   0.001

# Sigmoid parameters
# -------------------------------------
Vmin       =   0.0
Vmax       =  20.0
Vh         =  16.0
Vc         =   3.0

# Weights
Wmin, Wmax = 0.25, 0.75

# Gain of connections
# -------------------------------------
Cx_Str_cog 			= 	1.0
Cx_Str_mot 			= 	1.0
Cx_Str_ass 			= 	1.0
Cx_cog_Str_ass 		= 	0.2*np.ones((1,2*n+1))
Cx_mot_Str_ass 		= 	0.2*np.ones((2*n+1,1))

Cx_STN_cog 			= 	1.0
Cx_STN_mot 			= 	1.0

Str_Gpe_cog 		= 	-2.0
Str_Gpe_mot 		= 	-2.0
Str_ass_Gpe_cog 	= 	-2.0*np.ones((1,2*n+1))
Str_ass_Gpe_mot 	= 	-2.0*np.ones((2*n+1,1))

Str_Gpi_cog 		= 	-2.0
Str_Gpi_mot 		= 	-2.0
Str_ass_Gpi_cog 	= 	-2.0*np.ones((1,2*n+1))
Str_ass_Gpi_mot 	= 	-2.0*np.ones((2*n+1,1))

Gpe_STN_cog 		= 	-0.25*np.ones((2*n+1,1))
Gpe_STN_mot 		= 	-0.25*np.ones((1,2*n+1))

STN_Gpi_cog 		= 	1.0*np.ones((2*n+1,1))
STN_Gpi_mot 		= 	1.0*np.ones((1,2*n+1))

Cx_Th_cog 			= 	0.1
Cx_Th_mot 			= 	0.1

Th_Cx_cog			= 	0.4
Th_Cx_mot			= 	0.4

Gpi_Th_cog			= 	-0.25
Gpi_Th_mot			= 	-0.25

Cx_cog_cog = -0.5 * np.ones((2*n+1,1))
Cx_cog_cog[n,0] = 0.5
Cx_mot_mot = -0.5 * np.ones((1,2*n+1))
Cx_mot_mot[0,n] = 0.5
Cx_ass_ass = -0.5 * np.ones((2*n+1,2*n+1))
Cx_ass_ass[0,n] = 0.5
Cx_cog_ass = 0.025
Cx_mot_ass = 0.01
Cx_ass_cog = 0.01 * np.ones((1,2*n + 1))
Cx_ass_mot = 0.025 * np.ones((2*n + 1, 1))


