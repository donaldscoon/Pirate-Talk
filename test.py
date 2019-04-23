#!/usr/bin/env python3
"""tests for pirate-talk.py"""

from subprocess import getstatusoutput
from subprocess import getoutput
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
def test_play11():
    out = getoutput('{} -r 4 -s 4'.format(prg))
    expected = """
Cantankerous Tim says: Har, Har! Methinks you're a donkey-eared, scurvy-ridden, sack-o'maggots!!!

Black Spot Pete says: I have heard worse from'a fish, you're a pin-headed, scurvy-ridden, cabin-boy!!!

Cantankerous Tim says: Yer' a idiotic, knuckle-dragging, cow-pie!!!

Black Spot Pete says: Yer' a blathering, knuckle-dragging, swabber!!!

""".strip()
    assert out.strip() == expected
