from __future__ import print_function, division

__author__ = 'amrit'

import sys
import matplotlib.pyplot as plt
import numpy as np

sys.dont_write_bytecode = True

def draw(temp={}):
    font = {
        'size': 60}

    plt.rc('font', **font)
    paras = {'lines.linewidth': 10, 'legend.fontsize': 35, 'axes.labelsize': 60, 'legend.frameon': False,
             'figure.autolayout': True}
    plt.rcParams.update(paras)
    measures=['false_alarm', 'recall', 'precision', 'fscore', 'accuracy']

    measure_med = {}
    measure_iqr = {}
    for i in temp.keys():
        measure_med[i] = []
        measure_iqr[i] = []
    for learner,measure in temp.iteritems():
        measures=measure.keys()
        for mea,value in measure.iteritems():
            measure_med[learner].append(np.median(value))
            measure_iqr[learner].append(np.percentile(value, 75) - np.percentile(value, 25))

    plt.figure(num=0, figsize=(25, 15))
    M=1.0
    m=0.0
    plt.subplot(121)
    X = range(len(measures))
    #measures=['pf', 'rec', 'prec', 'f1', 'acc']
    for key in measure_iqr.keys():

        line,=plt.plot(X, measure_med[key],marker='*', markersize=20, label=str(key)+' median')
        plt.plot(X, measure_iqr[key], linestyle="-.", color=line.get_color(), markersize=20, label=str(key) + ' iqr')

    plt.ylim(m, M)
    plt.xticks(X, measures)
    plt.ylabel("Scores", labelpad=30)
    plt.xlabel("Measures", labelpad=30)
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc=2, borderaxespad=0.)
    plt.savefig("../results/Graph_less.png")