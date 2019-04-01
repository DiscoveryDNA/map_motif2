from MSE import *
import os
import sys

def bash_pipeline(alignment_file, motif_file, stand_cutoff=-50):
	"""
	alignment_file: alignment file path
	motif_file: motif file path
	stand_cutoff: score threshold (default no threshold)
	"""
	df = prelim_pipeline(alignment_file, motif_file)
	df.to_csv(os.path.basename(alignment_file) + "_" + os.path.basename(motif_file) + "_bash_output.csv")

# Takes the 2nd and 3rd strings from command line and uses them as arguments for bash_pipeline
bash_pipeline(sys.argv[1], sys.argv[2])