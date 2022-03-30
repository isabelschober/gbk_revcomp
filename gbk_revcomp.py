#! /usr/bin/python

import sys
import os
import argparse
from Bio import SeqIO
from Bio import SeqFeature

'''
By Isabel

Get the reverse complement of a GenBank record. 

The input files need to be single GenBank record files.

Usage: gbk_rev.py [-h] -i INPUTFILE

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        a single record GenBank file


'''

def main(argv):
	
	parser=argparse.ArgumentParser(description="by Isabel\n\nGet the reverse complement of a GenBank record.\nThe input files need to be single GenBank record files.", formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('-i', '--inputfile', required=True, help="a single record GenBank file")
	args = parser.parse_args()
	
	#input
	gbk_in=SeqIO.read(args.inputfile, "genbank")
	
	#reverse complement of sequence
	gbk_in.seq=gbk_in.seq.reverse_complement()
	length=len(gbk_in.seq)
	
	#new coordinates for features
	for feature in gbk_in.features:
		if feature.type=="source":
			pass
			
		else:
			
			if feature.location.strand==1:
				new_start=length-feature.location.start
				new_end=length-feature.location.end	
				new_strand=-1	
			elif feature.location.strand==-1:
				new_start=length-feature.location.start
				new_end=length-feature.location.end
				new_strand=1
				
			feature.location=SeqFeature.FeatureLocation(SeqFeature.ExactPosition(new_end),SeqFeature.ExactPosition(new_start),new_strand)
	
	#outout
	gbk_out=open(args.inputfile.replace(".gbk","").replace(".gbf","")+"_revcomp.gbk","w")
	gbk_out.write(gbk_in.format("genbank"))
	gbk_out.close()
	
	
if __name__ == "__main__":
   main(sys.argv)
