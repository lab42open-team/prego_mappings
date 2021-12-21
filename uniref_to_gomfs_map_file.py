#!/usr/bin/python

"""
This script builds the filtered_uniref50_gomfs.tsv file
including all the uniref : GO molecular functions pairs
"""

import sys

mapping_path = "/data/databases/mappings/"
ifile        = open(mapping_path + "uniref50_GOs.tsv", "r")
ffile        = open(mapping_path + "dict_go_molecular_function_ids.tsv", "r")
ofile        = open(mapping_path + "filtered_uniref50_GOs.tsv", "w")

set_of_gomf = set()
for line in ffile:
   set_of_gomf.add(line[:-1])

for line in ifile: 
   line    = line.split("\t")
   uniref  = line[0]
   gos     = line[1].split(";")
   gos[-1] = gos[-1][:-1]

   for go in gos: 

      if go in set_of_gomf: 

         ofile.write(uniref + "\t" + go + "\n")


"""
in the output file 
make sure the entries (lines) are unique! 
by running something like:
more filtered_uniref50_GOs | sort | uniq | sort > filtered_unique_uniref50_gomfs.tsv
"""
