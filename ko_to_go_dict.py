#!/usr/bin/python

"""
This script aims at building a .json file with keys 
the GO Molecular Functions terms and values all the KO 
terms related. 
"""


import sys
import json

set_of_gomf = set()
gomf_list   = open("/data/databases/mappings/dict_go_molecular_function_ids.tsv", "r")
for entry in gomf_list:
   set_of_gomf.add(entry[:-1])


triples   = open("/data/databases/mappings/GOs_KOs_via_Uniref50.tsv", "r")

ko_to_go = {}

counter = 0 
for triplet in triples:

   counter += 1 
   if counter % 100000 == 0: 
      print(str(counter) + " out of 142,771,206 triplets")

   triplet = triplet.split("\t")

   ko = triplet[1]
   go = triplet[0]


   if go in set_of_gomf:

      if ko not in ko_to_go.keys():

         ko_to_go[ko]      = {}
         ko_to_go[ko]['0'] = go

      else:

         index = str(len(ko_to_go[ko]))
         ko_to_go[ko][index] = go


with open('/data/databases/mappings/ko_togomfs.json', 'w') as f:
    json.dump(ko_to_go, f)






# counter      = 0 
# uniref_to_go = {}
# for triplet in triples:

#    counter += 1 
#    if counter % 100000 == 0: 
#       print(str(counter) + " out of 142,771,206 triplets")

#    triplet = triplet.split("\t")

#    uniref = triplet[2]
#    go     = triplet[0]


#    if go in set_of_gomf:

#       if uniref not in ko_to_go.keys():

#          uniref_to_go[uniref]      = {}
#          uniref_to_go[uniref]['0'] = go

#       else:

#          index = str(len(uniref_to_go[uniref]))
#          uniref_to_go[uniref][index] = go
      

# with open('/data/databases/mappings/uniref_togomfs.json', 'w') as f:
#     json.dump(uniref_to_go, f)


