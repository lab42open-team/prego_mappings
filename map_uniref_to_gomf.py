#!/usr/bin/python

"""
This script will build a json file having uniref ids as key
and their corresponding GO molecular function ids as their values
"""


import sys, os, json

ifile = sys.argv[1]

map_path = "/data/databases/mappings/"
map_file = open(map_path + "filtered_unique_uniref50_gomfs.tsv", "r")
map_dict = {}

counter = 0 ## 9,888,385 pairs
for pair in map_file: 
   counter   += 1
   if counter % 1000 == 0: 
      print(str(counter) + " out of 9,888,385 pairs have been parsed.")

   uniref, go = pair.split("\t")
   if uniref not in map_dict.keys():
      map_dict[uniref]      = {}
      map_dict[uniref]['0'] = go[:-1]
   else:
      index                   = str(len(map_dict[uniref]))
      map_dict[uniref][index] = go[:-1]



with open('uniref50_togomfs.json', 'w') as f:
    json.dump(map_dict, f)
