#!/usr/bin/python3

# d01.py
# AoC 2023 Day 01
# calibration vals
# bevan.lee@aurecongroup.com

import argparse, re

# argument parser
parser = argparse.ArgumentParser(description='AoC Day 01')
parser.add_argument('infile',  help='input filename')
args = parser.parse_args()

# read in whole file as list of strings with newlines stripped
with open(args.infile, 'r') as f:
    lines = f.read().splitlines()

# setup a map for nums spelled out in words
number_maps = {}
number_maps["one"] = 1
number_maps["two"] = 2
number_maps["three"] = 3
number_maps["four"] = 4
number_maps["five"] = 5
number_maps["six"] = 6
number_maps["seven"] = 7
number_maps["eight"] = 8
number_maps["nine"] = 9
for x in range(1,10):
    number_maps[str(x)] = x

calibration_values = []
match_expression_greedy = r'.*(\d|one|two|three|four|five|six|seven|eight|nine).*'
match_expression_lazy = r'.*?(\d|one|two|three|four|five|six|seven|eight|nine).*'
for line in lines:
    # greedy .* will make last digit the first match group
    last_digit = re.match(match_expression_greedy, line).group(1)
    # lazy .*? will make first digit the first match group
    first_digit = re.match(match_expression_lazy, line).group(1)
    calibration_values.append(int(str(number_maps[first_digit])+str(number_maps[last_digit])))

print(calibration_values)
print(sum(calibration_values))

