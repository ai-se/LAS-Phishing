from __future__ import print_function, division

__author__ = 'amrit'

import sys

sys.dont_write_bytecode = True

class DE(object):
    def __init__(self, F=0.3, CR=0.7, NP=10, GEN=5, Goal="Max", termination="Early"):
        self.F=F
        self.CR=CR
        self.NP=NP
        self.GEN=5
        self.GOAL=Goal
        self.termination=termination