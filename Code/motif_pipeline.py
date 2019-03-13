from MSE import *
import os
import sys

def bash_pipeline(alignment_file, motif_file, stand_cutoff=-50):
	"""
	alignment_file: shortened name of alignment file; for example "VT0809.fa"
	motif_file: motif file name, for example "bcd_FlyReg.fm"
	stand_cutoff: score threshold (default no threshold)
	"""
	df = prelim_pipeline(alignment_file, motif_file)
	df.to_csv(os.path.basename(alignment_file) + "_" + os.path.basename(motif_file) + "_bash_output.csv")
	# tacks on the alignment file name without ".fa" for the name of the csv output

bash_pipeline(sys.argv[1], sys.argv[2])