from __future__ import print_function, division

__author__ = 'amrit'

import sys
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_recall_fscore_support
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from random import shuffle
from ABCD import ABCD
from sklearn.ensemble import RandomForestClassifier
sys.dont_write_bytecode = True


def naive_bayes(train_inp, train_out, test_inp):
    model = GaussianNB().fit(train_inp, train_out)
    predicted = model.predict(test_inp)
    return model, predicted


def lin_svm(train_inp, train_out, test_inp):
    model = SVC(kernel='linear').fit(train_inp, train_out)
    predicted = model.predict(test_inp)
    return model, predicted


def rbf_svm(train_inp, train_out, test_inp):
    model = SVC(kernel='rbf').fit(train_inp, train_out)
    predicted = model.predict(test_inp)
    return model, predicted


def log_reg(train_inp, train_out, test_inp):
    model = LogisticRegression().fit(train_inp, train_out)
    predicted = model.predict(test_inp)
    return model, predicted


def dec_tree(train_inp, train_out, test_inp):
    model = DecisionTreeClassifier().fit(train_inp, train_out)
    predicted = model.predict(test_inp)
    return model, predicted

def knn(train_inp, train_out, test_inp):
    model = KNeighborsClassifier(n_neighbors=8).fit(train_inp, train_out)
    predicted = model.predict(test_inp)
    return model, predicted

def ran_forest(train_inp, train_out, test_inp):
    model = RandomForestClassifier().fit(train_inp, train_out)
    predicted = model.predict(test_inp)
    return model, predicted

def split(inp, out, n_folds):
    skf = StratifiedKFold(n_splits=n_folds, random_state=None, shuffle=True)
    inp, out = np.array(inp), np.array(out)
    for train_index, test_index in skf.split(inp, out):
        yield inp[test_index], out[test_index], inp[train_index], out[train_index]

def measures(actual, predicted, labels):
    return precision_recall_fscore_support(actual, predicted, labels=labels)

def run(corpus,label, target_class,classifier):
    print("***** %s *****" % classifier.__name__)
    splits = 5
    folds=5
    a,f,p,r,pf=[],[],[],[],[]
    corpus=np.array(corpus)
    label=np.array(label)
    for i in xrange(folds):
        "Shuffle"
        tmp = range(0, len(label))
        shuffle(tmp)
        corpus = corpus[tmp]
        label = label[tmp]
        for train_inp, train_out, test_inp, test_out in split(corpus, label, splits):
            model, predicted = classifier(train_inp, train_out, test_inp)
            labels=list(np.unique(test_out))
            abcd = ABCD(before=test_out, after=predicted)
            r1,_,p1,a1,f1,_,_,pf1=[k.stats() for k in abcd()][labels.index(target_class)]
            a.append(a1)
            r.append(r1)
            f.append(f1)
            p.append(p1)
            pf.append(pf1)

    return {"acc":a,"pre":p,"rec":r,"pf":pf,"f1":f}

def prediction(corpus,label,target_class):
    classifiers=[lin_svm,log_reg,naive_bayes,dec_tree,rbf_svm,knn,ran_forest]
    temp={}
    for i in classifiers:
        temp[i.__name__]=run(corpus,label,target_class, i)
    return temp
