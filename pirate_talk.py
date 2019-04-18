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

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument(
    #     'Name  ', metavar='str', help='What shall we call you, ya land lubber')

    # parser.add_argument(
    #     '-k',
    #     '--overlap',
    #     help='Number of codons to over lap at begining and end of sequence',
    #     metavar='int',
    #     type=int,
    #     default=3)

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

#---------------------------------------------------
def tim_says():



# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    word1 = """
    brainless stupid pin-headed blathering
    donkey-eared bleating idiotic
    cricket-sized pig-breathed
    """.strip().split()
    print(len(word1))

    word2 = """
    clam-toungued scurvy-ridden cross-eyed
    grog-abusing barnacle-backed yellow-bellied
    pus-faced twisted knuckle-dragging
    """.strip().split()
    print(len(word2))

    word3 = """
    waster-of-skin cabin-boy peice-of-filth
    whale-fart cow-pie bag-of-vomit
    sack-o'maggots anchor-head swabber
    """.strip().split()
    print(len(word3))


# --------------------------------------------------
if __name__ == '__main__':
    main()