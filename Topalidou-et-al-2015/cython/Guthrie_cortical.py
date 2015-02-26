# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License.
#
# Contributors: Nicolas P. Rougier (Nicolas.Rougier@inria.fr)
# -----------------------------------------------------------------------------
# References:
#
# * Interaction between cognitive and motor cortico-basal ganglia loops during
#   decision making: a computational study. M. Guthrie, A. Leblois, A. Garenne,
#   and T. Boraud. Journal of Neurophysiology, 109:3025–3040, 2013.
# -----------------------------------------------------------------------------
import numpy as np
from model import *
from display import *


def debug(time, cues, choice, reward):
    n = len(cues)
    cues = np.sort(cues)

    R.append(reward)
    if choice == cues[0]:
        P.append(1)
    else:
        P.append(0)

    print "Choice:         ",
    for i in range(n):
        if choice == cues[i]:
            print "[%d]" % cues[i],
        else:
            print "%d" % cues[i],
        if i < (n-1):
            print "/",
    if choice == cues[0]:
        print " (good)"
    else:
        print " (bad)"

    print "Reward (%3d%%) :   %d" % (int(100*CUE["reward"][choice]),reward)
    print "Mean performance: %.3f" % np.array(P).mean()
    print "Mean reward:      %.3f" % np.array(R).mean()
    print "Response time:    %d ms" % (time)
    print "CTX.cog->CTX.ass:", connections["CTX.cog -> CTX.ass"].weights
    print


n_experiments = 250
n_trials      = 150

if 1:
    for k in range(n_experiments):
        reset()
        learning = True
        P,RT = [], []
        connections["GPI.cog -> THL.cog"].active = True
        connections["GPI.mot -> THL.mot"].active = True

        for j in range(n_trials):
            reset_activities()
            # Settling phase (500ms)
            for i in xrange(0,500):
                iterate(dt)
            # Trial setup
            set_trial(n=2)
            # Learning phase (2500ms)
            for i in xrange(500,3000):
                iterate(dt)
                # Test if a decision has been made
                if CTX.mot.delta > decision_threshold:
                    RT.append(i-500)
                    cues, choice, reward = process(n=2, learning=learning)
                    cues = np.sort(cues)
                    if choice == cues[0]:
                        P.append(1)
                    else:
                        P.append(0)
                    break

            if j == 100:
                print "BG Performance:     %g" % np.mean(P)
                print "BG RT:              %g (+/- %g)"% (np.mean(RT), np.std(RT))
                P,RT = [], []
                # print "-------------------------------------------------------"
                learning = False
                connections["GPI.cog -> THL.cog"].active = False
                connections["GPI.mot -> THL.mot"].active = False

        print "Cortex Performance: %g" % np.mean(P)
        print "Cortex RT:          %g (+/- %g)"% (np.mean(RT), np.std(RT))
        print "CTX.cog->CTX.ass:", connections["CTX.cog -> CTX.ass"].weights
        print "CUE['value']:    ", CUE["value"]
        print "---"
