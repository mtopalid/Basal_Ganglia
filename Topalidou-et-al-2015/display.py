import matplotlib.pyplot as plt
from parameters import *

def subplot(rows,cols,n, alpha=0.0):
    ax = plt.subplot(rows,cols,n)

    #ax.patch.set_alpha(alpha)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.yaxis.set_ticks_position('left')
    ax.yaxis.set_tick_params(direction="outward")
    return ax

def figure(timesteps, cognitive, motor):

    fig = plt.figure(figsize=(12,5))
    plt.subplots_adjust(bottom=0.15)

    fig.patch.set_facecolor('.9')
    #ax = plt.subplot(2,2,number)

    plt.plot(timesteps[:-1], cognitive[0,0][:-1],c='b', label="Cognitive Cortex")
    plt.plot(timesteps[:-1], cognitive[0,1][:-1],c='b')
    plt.plot(timesteps[:-1], cognitive[0,2][:-1],c='b')
    plt.plot(timesteps[:-1], cognitive[0,3][:-1],c='b')

    plt.plot(timesteps[:-1], motor[0,0][:-1], c='r', label="Motor Cortex")
    plt.plot(timesteps[:-1], motor[0,1][:-1], c='r')
    plt.plot(timesteps[:-1], motor[0,2][:-1], c='r')
    plt.plot(timesteps[:-1], motor[0,3][:-1], c='r')

    plt.xlabel("Time (seconds)")
    plt.ylabel("Activity (Hz)")
    plt.legend(frameon=False, loc='upper left')
    plt.xlim(0.0,2.5)
    plt.ylim(-5.0,60.0)


    plt.xticks([0.0, 0.5, 1.0, 1.5, 2.5],
               ['0.0','0.5'+'\n(Trial start)','1.0','1.5', '2.5' + '\n(Trial stop)'])
    # plt.savefig("model-results.png")
    #plt.show()


def displayALL(timesteps, cognitive, motor, associative):

	fig = plt.figure(figsize=(17, 9))
	plt.subplots_adjust(bottom=0.15, hspace = 0.5)

	associative = associative.reshape(2,n,n,size)


	# STN motor
	# ---------
	ax = subplot(6,3,1)
	ax.set_title("MOTOR", fontsize=24)
	ax.set_ylabel("STN", fontsize=24)
	plt.plot(timesteps[:-1], motor[2,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], motor[2,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], motor[2,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], motor[2,3][:-1],c='m', label="4th")


	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# STN cognitive
	# -------------
	ax = subplot(6,3,2)
	ax.set_title("COGNITIVE", fontsize=24)
	plt.plot(timesteps[:-1], cognitive[2,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], cognitive[2,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], cognitive[2,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], cognitive[2,3][:-1],c='m', label="4th")


	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	ax = subplot(6,3,3,alpha=0)
	ax.set_title("ASSOCIATIVE", fontsize=24)
	ax.set_xticks([])
	ax.set_yticks([])
	ax.spines['left'].set_color('none')
	ax.patch.set_alpha(0.0)

	# Cortex motor
	# ------------
	ax = subplot(6,3,4)
	ax.set_ylabel("CORTEX", fontsize=24)
	plt.plot(timesteps[:-1], motor[0,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], motor[0,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], motor[0,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], motor[0,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# Cortex cognitive
	# ----------------
	ax = subplot(6,3,5)
	plt.plot(timesteps[:-1], cognitive[0,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], cognitive[0,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], cognitive[0,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], cognitive[0,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])


	# Cortex associative
	# ------------------
	ax = subplot(6,3,6)
	plt.plot(timesteps[:-1], associative[0,0,0][:-1],c='r', label="0 & 0")
	plt.plot(timesteps[:-1], associative[0,0,1][:-1],c='g', label="0 & 1")
	plt.plot(timesteps[:-1], associative[0,1,0][:-1],c='b', label="0 & 2")
	plt.plot(timesteps[:-1], associative[0,1,1][:-1],c='m', label="0 & 3")
	plt.plot(timesteps[:-1], associative[0,0,2][:-1],c='y', label="1 & 0")
	plt.plot(timesteps[:-1], associative[0,0,3][:-1],c='c', label="1 & 1")
	plt.plot(timesteps[:-1], associative[0,1,2][:-1],c='k', label="1 & 2")
	plt.plot(timesteps[:-1], associative[0,3,3][:-1],c='k', label="3 & 3")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# Striatum motor
	# --------------
	ax = subplot(6,3,7)
	ax.set_ylabel("STRIATUM", fontsize=24)
	plt.plot(timesteps[:-1], motor[1,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], motor[1,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], motor[1,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], motor[1,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# Striatum cognitive
	# ------------------
	ax = subplot(6,3,8)
	plt.plot(timesteps[:-1], cognitive[1,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], cognitive[1,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], cognitive[1,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], cognitive[1,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])



	# Striatum associative
	# --------------------
	ax = subplot(6,3,9)

	plt.plot(timesteps[:-1], associative[1,0,0][:-1],c='r', label="0 & 0")
	plt.plot(timesteps[:-1], associative[1,0,1][:-1],c='b', label="0 & 1")
	plt.plot(timesteps[:-1], associative[1,1,0][:-1],c='m', label="0 & 2")
	plt.plot(timesteps[:-1], associative[1,1,1][:-1],c='g', label="0 & 3")
	plt.plot(timesteps[:-1], associative[1,0,2][:-1],c='y', label="1 & 0")
	plt.plot(timesteps[:-1], associative[1,0,3][:-1],c='c', label="1 & 1")
	plt.plot(timesteps[:-1], associative[1,1,2][:-1],c='k', label="1 & 2")
	plt.plot(timesteps[:-1], associative[1,3,3][:-1],c='k', label="3 & 3")


	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# GPe motor
	# ---------
	ax = subplot(6,3,10)
	ax.set_ylabel("GPe", fontsize=24)

	plt.plot(timesteps[:-1], motor[3,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], motor[3,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], motor[3,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], motor[3,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# GPe cognitive
	# -------------
	ax = subplot(6,3,11)
	plt.plot(timesteps[:-1], cognitive[3,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], cognitive[3,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], cognitive[3,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], cognitive[3,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# GPi motor
	# ---------
	ax = subplot(6,3,13)
	ax.set_ylabel("GPi", fontsize=24)

	plt.plot(timesteps[:-1], motor[4,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], motor[4,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], motor[4,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], motor[4,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# GPi cognitive
	# -------------
	ax = subplot(6,3,14)
	plt.plot(timesteps[:-1], cognitive[4,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], cognitive[4,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], cognitive[4,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], cognitive[4,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# Thalamus motor
	# --------------
	ax = subplot(6,3,16)
	ax.set_ylabel("THALAMUS", fontsize=24)
	plt.plot(timesteps[:-1], motor[5,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], motor[5,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], motor[5,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], motor[5,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# Thalamus cognitive
	# ------------------
	ax = subplot(6,3,17)
	plt.plot(timesteps[:-1], cognitive[5,0][:-1],c='r', label="1st")
	plt.plot(timesteps[:-1], cognitive[5,1][:-1],c='g', label="2nd")
	plt.plot(timesteps[:-1], cognitive[5,2][:-1],c='b', label="3rd")
	plt.plot(timesteps[:-1], cognitive[5,3][:-1],c='m', label="4th")

	plt.xticks([0.0, 0.5, 1.0, 1.5, 3.0, duration],
               ['0.0','0.5\n(Trial start)','1.0','1.5', '3.0\n(Trial stop)', duration])

	# plt.savefig("model-results-all.pdf")
	#plt.show()
