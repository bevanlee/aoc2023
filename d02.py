#!/usr/bin/python3

# d02.py
# AoC 2023 Day 02
# Cube game
# bevan.lee@aurecongroup.com

import argparse, re

# functions
# checks if draw is possible
def check_draw(bag, draw):
    for colour in draw:
        if draw[colour] > bag[colour]:
            return False
    return True

# checks if game is valid
def check_game(bag, draws):
    for draw in draws:
        if not check_draw(bag, draw):
            return False
    return True

# recursive function to give minimum cube amounts for a successful game
def minimum_possible(bag, draws):
    if draws:
        draw = draws.pop()
        for colour in draw:
            if draw[colour] > bag[colour]:
                bag[colour] = draw[colour]
        bag = minimum_possible(bag, draws)
    return bag

# calculate the power value for a min bag
def calculate_power(bag):
    power = 1
    for colour in bag:
        power *= bag[colour]
    return power

# argument parser
parser = argparse.ArgumentParser(description='AoC Day 01')
parser.add_argument('infile',  help='input filename')
args = parser.parse_args()

# read in whole file as list of strings with newlines stripped
with open(args.infile, 'r') as f:
    lines = f.read().splitlines()

# vars
bag_contents = { "red" : 12, "green" : 13, "blue" : 14 }
valid_ids = []
powers = []

# iterate over games
for line in lines:
    # seperate out the id and the main string
    m = re.match(r"^Game (\d+): (.*)", line)
    game_num = m.group(1)
    game_draws = m.group(2)
    # split into list of rounds
    game = game_draws.split(";")
    # clean up data structure
    game_clean = []
    for draws in game:
        # split colours
        draw = draws.split(",")
        draw_dict = {}
        # repack as dictionary
        for cube_type in draw:
            num_cubes, colour = cube_type.strip().split()
            draw_dict[colour] = int(num_cubes)
        # add into the clean list
        game_clean.append(draw_dict)
    # check if valid and add to list
    if check_game(bag_contents, game_clean):
        valid_ids.append(int(game_num))
    # compute min number cubes
    min_bag = {"red":0,"green":0,"blue":0}
    min_bag = minimum_possible(min_bag, game_clean)
    # compute power
    powers.append(calculate_power(min_bag))
# outputs
print("Valid IDs list:, ", valid_ids)
print("Sum of valid IDs: ", sum(valid_ids))
print("Powers list:, ", powers)
print("Sum of powers: ", sum(powers))

