#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
# add the s argument to input a sequence, make it required and specify that it should be a string
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
# add the -m argument to search a motif in the sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper()

if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq): # if it contains T and U the sequence is wrong
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq): # if it contains U and T the sequence is wrong
        print ('The sequence is RNA')
    elif re.search('T', args.seq) and re.search('U', args.seq): # different message for when the seq has both U and T
        raise ValueError('Sequence invalid: The sequence contains both T and U')
    else:
        print ('The sequence can be DNA or RNA')

    # compute the percentage of each nucleotide in the sequence
    for nt in 'ACGTU':
        print(f'{nt}: {args.seq.count(nt) / len(args.seq) * 100:.2f}%')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")