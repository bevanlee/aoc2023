#!/usr/bin/python3

# d02.py
# AoC 2023 Day 02
# 
# bevan.lee@aurecongroup.com

import argparse, re

# argument parser
parser = argparse.ArgumentParser(description='AoC Day 01')
parser.add_argument('infile',  help='input filename')
args = parser.parse_args()

# read in whole file as list of strings with newlines stripped
with open(args.infile, 'r') as f:
    lines = f.read().splitlines()

