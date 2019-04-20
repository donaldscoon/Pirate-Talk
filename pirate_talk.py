#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-11
Purpose: Engage in Verbal Fisticuffs, Pirate Style
"""

import argparse
import sys
import os
import re
import random
import time

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-r',
        '--rounds',
        help='Number of rounds in the insult competition',
        metavar='int',
        type=int,
        required=True)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    rounds = args.rounds

    if rounds < 0:
        die('"{}" must be greater than zero'.format(rounds))

    word1 = """
    brainless stupid pin-headed blathering
    donkey-eared bleating idiotic
    cricket-sized pig-breathed
    """.strip().split()

    word2 = """
    clam-toungued scurvy-ridden cross-eyed
    grog-abusing barnacle-backed yellow-bellied
    pus-faced twisted knuckle-dragging
    """.strip().split()

    word3 = """
    waste-of-skin cabin-boy peice-of-filth
    whale-fart cow-pie bag-of-vomit
    sack-o'maggots anchor-head swabber
    """.strip().split()

    starters = ['Yer\' a', 
                'That be true enough, but yer a', 
                'You\'re a', 
                'Har, Har! Methinks you\'re a', 
                'Ha! You insult like a child. You\'re a',
                'Is that the best you got? You\'re a',
                'My fresh born lass swears better you, yer a',
                'I have heard worse from\'a fish, you\'re a',
                'Out of ideas? HA! Yer a']

    tim = 'Cantankerous Tim says:'
    pete = 'Black Spot Pete says:'

    for i in range(rounds):
        start = random.choice(starters)
        w1 = random.choice(word1)
        w2 = random.choice(word2)
        w3 = random.choice(word3)
        if int(i) % 2 == 0:
            print('{} {} {}, {}, {}!!!\n'.format(tim, start, w1, w2, w3))
            time.sleep(5)
        else:
            print('{} {} {}, {}, {}!!!\n'.format(pete, start, w1, w2, w3))
            time.sleep(5)

    """future implementation make it go through
       every possible combo without replication."""

    if rounds > (9*9*9):
        print('That\'s how you swear like a sailor')


# --------------------------------------------------
if __name__ == '__main__':
    main()