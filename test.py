#!/usr/bin/env python3
"""tests for pirate-talk.py"""

from subprocess import getstatusoutput
import os
import random
import re
import string
import sys

prg = 'pirate_talk.py'

# --------------------------------------------------
def test_usage():
    rv, out = getstatusoutput('{}'.format(prg))
    assert rv != 0
    assert out.lower().startswith('usage')

# # -------------------------------------------------
# def run_it():
#     """run the program"""y
#     def test_bad_input():
#     """fails on bad input"""

#     for pct in [-1, 101]:
#         rv, out = getstatusoutput('{} -p {} fasta'.format(prg, pct))
#         assert rv > 0
#         assert out == '--pct_gc "{}" must be between 0 and 100'.format(pct)