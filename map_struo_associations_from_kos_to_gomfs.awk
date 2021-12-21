#! /usr/bin/gawk -f

## USAGE:
## ./extract_struo_associations.awk
## /data/databases/struo/metadata_1per-GTDB-Spec_gte50comp-lt5cont_wtaxID.tsv  \
## /data/databases/mappings/filtered_unique_uniref50_gomfs.tsv \
## /data/databases/struo/struo_to_go/ncbi_uniref_genomes/genomes_rest.tsv  > struo_database_pairs.tsv

BEGIN {
   -F"\t"
}

(ARGIND=1 && NR>1) {
   ncbid_gids[$74] = ncbid_gids[$74] ? ncbid_gids[$74] "+" $56 : $56
}
(ARGIND=2)  {
   uniref[$1] = (uniref[$1]? uniref[$1] FS $2 : $2)
}
(ARGIND=3)  {
   if ($2 in uniref) {
      split(uniref[$2], a,"\t") ;
      for (go in a) {
         print "-2\t" $1 "\t-23\t" a[go] "\tStruo\tGenome annotation\t50\tTRUE\thttps://www.ncbi.nlm.nih.gov/assembly/?term=" ncbid_gids[$1] ;
         print "-23\t" a[go] "\t-2\t" $1 "\tStruo\tGenome annotation\t50\tTRUE\thttps://www.ncbi.nlm.nih.gov/assembly/?term=" ncbid_gids[$1]
      }
   }
}
