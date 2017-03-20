from __future__ import print_function, division

__author__ = 'amrit'

import re
import sys
import pandas as pd
from collections import OrderedDict
import numpy as np
sys.dont_write_bytecode = True
import Learners
from draw import draw
import pickle

class Csv(object):
    """docstring for Csv"""
    def __init__(self, csvFileName):
        self.csvFileName = csvFileName
        self.next = self.parse().next()

    def parse(self):
        """
        Convert rows of strings to ints,floats, or strings
        as appropriate
        """

        def atoms(lst):
            return map(atom, lst)

        def atom(x):
            try:
                return int(x)
            except:
                try:
                    return float(x)
                except ValueError:
                    return x

        for row in self.rows(prep=atoms):
            yield row

    def rows(self, prep=None,
             whitespace='[\n\r\t]',
             comments='#.*',
             sep=","
             ):
        """
        Walk down comma seperated values,
        skipping bad white space and blank lines
        """
        doomed = re.compile('(' + whitespace + '|' + comments + ')')
        with open(self.csvFileName) as fs:
            for line in fs:
                line = re.sub(doomed, "", line)
                if line:
                    row = map(lambda z: z.strip(), line.split(sep))
                    if len(row) > 0:
                        yield prep(row) if prep else row

class Table:
    def __init__(self, csv_file):
        self.csv = csv_file
        self.rows = []

    """
        Walk down comma seperated values,
        skipping bad white space and blank lines
        """
    def add_rows(self, csv_file):
        csv = Csv(csv_file)
        rows=[]
        data = OrderedDict()
        for num, row in enumerate(csv.parse()):
            rows.append(row)
        for x in zip(*rows):
            data[x[0]]=list(x[1:])
        return data

def show_stats(data,col_no=0):
    try:
        col_no=int(col_no)
    except:
        return "Not Integer"
    if col_no==0 or col_no>len(data.columns):
        return "Column Number is not within range"
    elif data[data.columns[col_no-1]].dtype==np.int64 or data[data.columns[col_no-1]].dtype==np.float64:
        string="Mean, Median, Std Deviation and Variance of "+ str(data.columns[col_no-1])+\
                ": "+ str(data[data.columns[col_no-1]].mean())+", "+\
        str(data[data.columns[col_no - 1]].median())+", "+ str(data[data.columns[col_no - 1]].std())+\
        ", " + str(data[data.columns[col_no - 1]].var())# median, std, var
        return string
    else:
        string="Count of values: \n"+ str(pd.value_counts(data[data.columns[col_no - 1]]))
        return string

def encode_target(df):
    df_mod = df.copy()
    target_class=0
    for i in df.columns:
        if df[i].dtype==object:
            df_mod = df_mod.copy()
            targets = df_mod[i].unique()
            if i=='loan_status':
                target_class=list(targets).index('Fully Paid')
            map_to_int = {name: n+1 for n, name in enumerate(targets)}
            df_mod[i] = df_mod[i].replace(map_to_int)
    return df_mod, target_class+1

def corpus_labels(corpus,target_column,target_class):
    data=[]
    labels=[]
    for x in corpus:
        data.append(x[:target_column])
        labels.append(x[target_column])
    labels=[1 if x==target_class else -1 for x in labels]
    return data,labels

if __name__ == '__main__':

    data = '../dataset/training.csv'
    table = Table(data)
    data=table.add_rows(data)
    df=pd.DataFrame(data)

    ## replace missing values with nan
    df=df.replace(r'', np.nan, regex=True)
    df.fillna(0,inplace=True)
    target_class=1
    df=df[['Prefix_Suffix', 'having_Sub_Domain', 'SSLfinal_State', 'Request_URL', 'URL_of_Anchor',
           'Links_in_tags', 'SFH', 'web_traffic', 'Google_Index', 'Result']]
    ## with all features
    '''target_column=df.columns.get_loc("Result")
    data=df.values.tolist()
    corpus,label=corpus_labels(data,target_column,target_class)

    temp=Learners.prediction(np.asarray(corpus),np.asarray(label),target_class)
    with open('../dump/result.pickle', 'wb') as handle:
        pickle.dump(temp, handle)
    #with open('../dump/result.pickle', 'rb') as handle:
    #    temp = pickle.load(handle)
    draw(temp)'''

    ## with subset of features
    target_column = df.columns.get_loc("Result")
    data = df.values.tolist()
    corpus, label = corpus_labels(data, target_column, target_class)

    temp = Learners.prediction(np.asarray(corpus), np.asarray(label), target_class)
    with open('../dump/result1.pickle', 'wb') as handle:
        pickle.dump(temp, handle)
    # with open('../dump/result.pickle', 'rb') as handle:
    #    temp = pickle.load(handle)
    draw(temp)
