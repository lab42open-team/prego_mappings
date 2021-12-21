#!/usr/bin/gawk -f

## USAGE:
## ./extract_jgj_mgrast_associations.awk /data/databases/mappings/gomfs_to_kos.tsv /data/experiments/jgi_associations.tsv > gomf_jgi_associations.tsv
## where paired_associations.tsv the associations files, e.g. jgi_associations.tsv


BEGIN {
	FS  = "\t"
}

(ARGIND==1) {
	ko_to_gomfs[$2] = ko_to_gomfs[$2] ? ko_to_gomfs[$2] FS $1 : $1
}

(ARGIND==2) {

   split($8, a, "|"); 

   for (i in a){

      split(a[i], b, ":")

      ko_term   = b[1]
      abundance = b[2]

      if ( ko_term in ko_to_gomfs) {

         split(ko_to_gomfs[ko_term], c, "\t") ;

         for (j in c) {

            gos[c[j]] += abundance

         }
      } 
   }

   for (k in gos){
      d = d k ":" gos[k] "|"
   }

   print $1 "\t" $2 "\t" $3 "\t" $4 "\t" $5 "\t" $6 "\t" $7 "\t" substr(d, 1, length(d)-1) ;

   delete gos
   d = ""
}


