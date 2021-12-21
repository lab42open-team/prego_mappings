#!/usr/bin/python 

import sys, os
import getopt


def main(filename): 

   filename        = open(filename, "r")
   mappings_path   = "/data/databases/mappings/"

   counter = 0 

   for line in filename: 

      counter += 1 
      print("counter: " + str(counter))

      three_cols_file = open(mappings_path + "GOs_KOs_via_Uniref50.tsv","r")
      only_gomf_file  = open(mappings_path + "dict_go_molecular_function_ids.tsv","r")

      ko   = ''
      line = line.split("\t")

      if line[0] == "-90":  
         
         ko = line[1]
      
      elif line[2] == "-90": 

         ko = line[3]

      else: 
         continue

      ko_term = ko[3:]

   
      for triplet in three_cols_file: 
         
         triplet = triplet.split("\t")

         if ko_term == triplet[1]: 
            
            potential_go = triplet[0] 
            print(ko_term, potential_go)

            for entry in only_gomf_file: 
               
               print(entry)
               if entry[:-1] == potential_go: 

                  print("Convert: " + ko_term + " to: " + triplet[0])



if __name__ == '__main__': 


   opts, args = getopt.getopt(sys.argv[1:], "i:o:", ["input=", "output="])
   current_directory = os.getcwd()

   for i in opts:

      if i[0] == "--input" or i[0] == "-i":
         ifile = i[1]
         # ifile = current_directory + "/" + dir_path

      elif i[0] == "--output" or i[0] == "-o":
         output_file = current_directory + "/" + i[1]


   main(ifile)