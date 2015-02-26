from dana import *
from parameters import *

def sigmoid(V,Vmin=Vmin,Vmax=Vmax,Vh=Vh,Vc=Vc):
    return  Vmin + (Vmax-Vmin)/(1.0+np.exp((Vh-V)/Vc))

def noise(Z, level):
    Z = (1+np.random.uniform(-level/2,level/2,Z.shape))*Z
    return np.maximum(Z,0.0)

# Populations
# -----------------------------------------------------------------------------
def populations():

	Cortex_cog   = zeros((n,1), """dV/dt = (-V + I + Iext - Cortex_h)/(Cortex_tau);
							   U = noise(V,Cortex_N); I; Iext""")#min_max(V,-3.,60.)
	Cortex_mot   = zeros((1,n), """dV/dt = (-V + I + Iext - Cortex_h)/(Cortex_tau);
							   U = noise(V,Cortex_N); I; Iext""")
	Cortex_ass   = zeros((n,n), """dV/dt = (-V + I + Iext - Cortex_h)/(Cortex_tau);
							   U = noise(V,Cortex_N); I; Iext""")
	Striatum_cog = zeros((n,1), """dV/dt = (-V + I - Striatum_h)/(Striatum_tau);
							   U = sigmoid(noise(V, Striatum_N)); I""")
	Striatum_mot = zeros((1,n), """dV/dt = (-V + I - Striatum_h)/(Striatum_tau);
							   U = sigmoid(noise(V, Striatum_N)); I""")
	Striatum_ass = zeros((n,n), """dV/dt = (-V + I - Striatum_h)/(Striatum_tau);
							   U = sigmoid(noise(V, Striatum_N)); I""")
	STN_cog      = zeros((n,1), """dV/dt = (-V + I - STN_h)/(STN_tau);
							   U = noise(V,STN_N); I""")
	STN_mot      = zeros((1,n), """dV/dt = (-V + I - STN_h)/(STN_tau);
							   U = noise(V,STN_N); I""")
	GPe_cog      = zeros((n,1), """dV/dt = (-V + I - GPe_h)/(GPe_tau);
							   U = noise(V,GPe_N); I""")
	GPe_mot      = zeros((1,n), """dV/dt = (-V + I - GPe_h)/(GPe_tau);
							   U = noise(V,GPe_N); I""")#noise(V,GPe_N)
	GPi_cog      = zeros((n,1), """dV/dt = (-V + I - GPi_h)/(GPi_tau);
							   U = noise(V,GPi_N); I""")
	GPi_mot      = zeros((1,n), """dV/dt = (-V + I - GPi_h)/(GPi_tau);
							   U = noise(V,GPi_N); I""")
	Thalamus_cog = zeros((n,1), """dV/dt = (-V + I - Thalamus_h)/(Thalamus_tau);
							   U = noise(V,Thalamus_N); I""")
	Thalamus_mot = zeros((1,n), """dV/dt = (-V + I - Thalamus_h)/(Thalamus_tau);
							   U = noise(V, Thalamus_N); I""")

	return Cortex_cog, Cortex_mot, Cortex_ass, Striatum_cog, Striatum_mot, Striatum_ass, STN_cog, STN_mot, GPe_cog, GPe_mot, GPi_cog, GPi_mot, Thalamus_cog, Thalamus_mot


