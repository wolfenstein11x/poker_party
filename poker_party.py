#!/usr/bin/env python3

from random import shuffle
import math

players = ["Greg", "Litte Jonny", "Steph", "Liz", "Patrick", "Jo-Ann", "Paul", "Polly", "Will", "Elliot", "Eric", "Danny B.", "Bob", "Bryce", "Mr Carr", "Dave Calvin", "Cameron", "Kevin", "Charles", "Blair", "Shannon", "Sheldon", "Daniel"]

players_per_table = 4

num_tables = math.ceil(len(players) / players_per_table)

shuffle(players)

idx = 0
table_count = 1

while (idx < len(players)):
    if ((idx % players_per_table) == 0):
        print("\nTable " + str(table_count), end=': ')
        table_count += 1
    print(players[idx], end=', ')
    idx += 1

print("\n")
