from __future__ import print_function, division

__author__ = 'amrit'

import sys
from train import Table, corpus_labels
import pandas as pd
from regex import *
import csv
import numpy as np
from random import shuffle

sys.dont_write_bytecode = True

def read_csv_pos(file='../dataset/verified_online.csv'):
    table = Table(file)
    _,rows = table.add_rows(file)
    csvfile=open('../dataset/phistank+features.csv', 'wb')
    csvwriter=csv.writer(csvfile, delimiter=',')
    for i,x in enumerate(rows):
        if i!=0:
            if x[-1].lower()!='other':
                str = x[1].lower()
                try:
                    request = urllib2.Request(str)
                    response = urllib2.urlopen(request).read()
                    ## Feature extraction
                    l=process(response,str,pref_suffix,multi_subdomain,request_url,url_anchor,links_in_tags,SFH,google_index)
                    print(l)
                    ## Class label
                    l.append(1)
                    csvwriter.writerow(l+[str]+[x[-1]])
                except:
                    print("can not open: "+str)
        elif i==0:
            csvwriter.writerow(['Prefix_Suffix', 'having_Sub_Domain', 'Request_URL', 'URL_of_Anchor',
           'Links_in_tags', 'SFH', 'Google_Index', 'Result', 'URL', 'Target'])
    csvfile.close()
    #df = pd.DataFrame(data)
    #print(df.columns.values.tolist())

def read_csv_neg(file='../dataset/phistank-urls.csv'):
    table = Table(file)
    _,rows = table.add_rows(file)
    csvfile=open('../dataset/phistank-features.csv', 'wb')
    csvwriter=csv.writer(csvfile, delimiter=',')
    for i,x in enumerate(rows):
        if i!=0:
            if x[0].lower()!='other':
                str = x[1].lower()
                try:
                    request = urllib2.Request(str)
                    response = urllib2.urlopen(request).read()
                    ## Feature extraction
                    l=process(response,str,pref_suffix,multi_subdomain,request_url,url_anchor,links_in_tags,SFH,google_index)
                    print(l)
                    ## Class label
                    l.append(-1)
                    csvwriter.writerow(l+[str]+[x[0]])
                except:
                    print("can not open: "+str)
        elif i==0:
            csvwriter.writerow(['Prefix_Suffix', 'having_Sub_Domain', 'Request_URL', 'URL_of_Anchor',
           'Links_in_tags', 'SFH', 'Google_Index', 'Result', 'URL', 'Target'])
    csvfile.close()
    #df = pd.DataFrame(data)
    #print(df.columns.values.tolist())

def features_read(file='../dataset/features.csv'):
    table = Table(file)
    data,_ = table.add_rows(file)
    df = pd.DataFrame(data)
    ## replace missing values with nan
    df = df.replace(r'', np.nan, regex=True)
    df.fillna(0, inplace=True)
    target_class = 1
    df = df[['Prefix_Suffix', 'having_Sub_Domain', 'Request_URL', 'URL_of_Anchor',
             'Links_in_tags', 'SFH', 'Google_Index', 'Result']]
    target_column = df.columns.get_loc("Result")
    data = df.values.tolist()
    test_data, test_labels = corpus_labels(data, target_column, target_class)
    return test_data,test_labels

def gen_testing_phistank(file='../dataset/phistank.csv'):
    table = Table(file)
    data, _ = table.add_rows(file)
    df = pd.DataFrame(data)
    ## replace missing values with nan
    df = df.replace(r'', np.nan, regex=True)
    df.fillna(0, inplace=True)
    headers=['Prefix_Suffix', 'having_Sub_Domain', 'Request_URL', 'URL_of_Anchor',
             'Links_in_tags', 'SFH', 'Google_Index', 'Result','Target']
    df = df[headers]

    targets=['PayPal', 'Facebook','AOL','Google','Microsoft','Apple','Yahoo','Dropbox']
    # data=df[df['Target'] == 'Dropbox'].values.tolist()
    # data=zip(*zip(*data)[:-1])
    # shuffle(data)
    for i in targets:
        data=df[df['Target'].str.lower() == i.lower()].values.tolist()
        with open('../dataset/testing/'+i+'.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerow(headers[:-1])
                data=zip(*zip(*data)[:-1])
                shuffle(data)
                writer.writerows(data)

gen_testing_phistank()
#read_csv_neg()
#features_read()