from parameters import *

def debug(cgchoice, c1, c2, P = None, reward = None, R = None, time = None):

    print "Choice:         ",
    if cgchoice == c1:
		print " 	[%d]" % c1,
    else:
		print " 	%d" % c1,

    if cgchoice == c2:
		print " [%d]" % c2,
    else:
		print " %d" % c2,

    if cgchoice == np.minimum(c1,c2):
        print " (good)"
    else:
        print " (bad)"

    if reward is not None:
    	print "Reward	  		: %d" % (reward)
    	print "Mean reward		: %.3f" % np.array(R).mean()
    if P is not None:
    	print "Mean performance	: %.3f" % np.array(P).mean()
    	#print "15 trials performance	: %.3f" % np.array(P[-15:]).mean()
    if time is not None:
	    print "Response time:		%d ms" % (time*1000)
    #print "CTX.cog->CTX.ass:", connections["CTX.cog -> CTX.ass"].weights

def debug_weights(W_cx_cog, W_cx_mot, W_str):
	print "Cortex Cognitive"
	print "[%.4f %.4f %.4f %.4f" %(W_cx_cog.weights[0][0], W_cx_cog.weights[4][1], W_cx_cog.weights[8][2], W_cx_cog.weights[12][3])
	print " %.4f %.4f %.4f %.4f" %(W_cx_cog.weights[1][0], W_cx_cog.weights[5][1], W_cx_cog.weights[9][2], W_cx_cog.weights[13][3])
	print " %.4f %.4f %.4f %.4f" % (W_cx_cog.weights[2][0], W_cx_cog.weights[6][1], W_cx_cog.weights[10][2], W_cx_cog.weights[14][3])
	print " %.4f %.4f %.4f %.4f]" %(W_cx_cog.weights[3][0], W_cx_cog.weights[7][1], W_cx_cog.weights[11][2], W_cx_cog.weights[15][3])
	if 0:
		print "Cortex Motor"
		print "[%.4f %.4f %.4f %.4f" %(W_cx_mot.weights[0][0], W_cx_mot.weights[1][1], W_cx_mot.weights[2][2], W_cx_mot.weights[3][3])
		print " %.4f %.4f %.4f %.4f" %(W_cx_mot.weights[4][0], W_cx_mot.weights[5][1], W_cx_mot.weights[6][2], W_cx_mot.weights[7][3])
		print " %.4f %.4f %.4f %.4f" % (W_cx_mot.weights[8][0], W_cx_mot.weights[9][1], W_cx_mot.weights[10][2], W_cx_mot.weights[11][3])
		print " %.4f %.4f %.4f %.4f]" %(W_cx_mot.weights[12][0], W_cx_mot.weights[13][1], W_cx_mot.weights[14][2], W_cx_mot.weights[15][3])
	print "Striatum"
	print "[%.4f %.4f %.4f %.4f]\n" % (W_str.weights[0][0], W_str.weights[1][1], W_str.weights[2][2], W_str.weights[3][3])

