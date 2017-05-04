#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_lace
----------------------------------

Tests for `lace` module.
"""

import unittest
import csv
from CLIFF import *
from MORPH import *

class RunLace():
    def setUp(self):
        #with open('../tests/sample_data/school.csv', 'r') as f:
        with open('../../dataset/uci_training.csv', 'r') as f:
            reader = csv.reader(f)
            self.header = next(reader)
            self.data = list()
            for line in reader:
                self.data.append(line)

    def test_something(self,cliff_percentage=0.1, alpha=0.3, beta=0.5):
        # testing cliff
        aftercliff = cliff(self.header,
                self.data,
                ['Prefix_Suffix','having_Sub_Domain','Request_URL','URL_of_Anchor','Links_in_tags','SFH','Google_Index'],
                'Result',
                False,
                cliff_percentage)
        print(aftercliff[0])
        aftermorph = morph(self.header,
                         aftercliff,
                        ['Prefix_Suffix', 'having_Sub_Domain', 'Request_URL', 'URL_of_Anchor', 'Links_in_tags',
                            'SFH', 'Google_Index'],
                           'Result',
                          True,
                          False,
                          alpha,
                          beta)
        print(aftermorph[0])
        self.results=aftermorph

    def write_csv(self, pathname):
        with open(pathname, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            writer.writerows(self.results)

    def tearDown(self):
        pass

test=RunLace()
cliff_percentage=0.1
alpha=0.2
beta=0.8
test.setUp()
test.test_something(cliff_percentage=cliff_percentage, alpha=alpha, beta=beta)
test.write_csv('../../dataset/training/laced_training_'+str(cliff_percentage)+'_' +str(alpha)+'_'+str(beta)+'.csv')
