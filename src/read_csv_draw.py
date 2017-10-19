from __future__ import print_function, division

__author__ = 'amrit'

import sys

sys.dont_write_bytecode = True
import pandas as pd
import matplotlib.pyplot as plt



def draw(baseline,lace,f):
    font = {
        'size': 60}

    plt.rc('font', **font)
    paras = {'lines.linewidth': 10, 'legend.fontsize': 35, 'axes.labelsize': 60, 'legend.frameon': True,
             'figure.autolayout': True}
    plt.rcParams.update(paras)

    fig=plt.figure(num=0, figsize=(25, 15))
    x_labels = ['acc', 'pre', 'auc', 'f1', 'pf', 'rec']
    plt.subplot(121)
    X = range(len(x_labels))
    for a,i  in enumerate(baseline):
        line, = plt.plot(X, i[1:],linestyle="-.", marker='D', markersize=15, label=str(i[0]))
        plt.plot(X, lace[a][1:], color=line.get_color(),marker='*', markersize=20, label=str(lace[a][0]))

    plt.xticks(X, x_labels)
    plt.ylabel("Scores", labelpad=30)
    plt.xlabel("Measures", labelpad=30)
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc=2, borderaxespad=0.)
    plt.savefig("../results/" + f + "_raw.png")
    plt.close(fig)

def main():
    files = ['AOL', 'Facebook', 'PayPal', 'Google', 'Apple', 'Yahoo']
    for i in files:
        df = pd.read_csv("../results/"+i+".csv")

        df_baseline = df[df['learners'].str.contains("b_")].values.tolist()
        df_lace = df[df['learners'].str.contains("l_")].values.tolist()
        draw(df_baseline,df_lace,i)
main()