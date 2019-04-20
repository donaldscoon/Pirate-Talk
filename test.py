#!/usr/bin/env python3
"""tests for pirate-talk.py"""

from subprocess import getstatusoutput
import os
import random
import re
import string
import sys

prg = './pirate_talk.py'

# --------------------------------------------------
def test_usage():
    rv, out = getstatusoutput('{}'.format(prg))
    assert rv != 0
    assert out.lower().startswith('usage')

# --------------------------------------------------
def test_bad_number():
    for r in [-1, 10]:
        rv, out = getstatusoutput('{} -r {}'.format(prg, r))
        assert rv > 0
        assert out == ('"{}" must be greater than zero'.format(r))



# # -------------------------------------------------
# def run_it():
#     """run the program"""y
#     def test_bad_input():
#     """fails on bad input"""
