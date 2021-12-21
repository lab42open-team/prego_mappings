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

	if ($1=="-90") {

#		gsub(/^.\{3\}/, "", $2) ;
		$2 = substr($2, 4)

		if ( $2 in ko_to_gomfs) {

			split(ko_to_gomfs[$2], a, "\t") ;

			for (i in a) {

				print "-23" "\t" a[i] "\t" $3 "\t" $4 "\t" $5 "\t" $6 "\t" $7 "\t" $8 "\t" $9 ;
				print $3 "\t" $4 "\t" "-23" "\t" a[i] "\t" $5 "\t" $6 "\t" $7 "\t" $8 "\t" $9
			}
		}
	} if ($3=="-90") {

		check=1

	} if ($1 != "-90" && $3 != "-90") {
		print $0
	}
}
