from MSE import *
import os

def bash_pipeline(alignment_file, motif_file, stand_cutoff=-50):
	"""
	alignment_file: alignment file path
	motif_file: motif file path
	stand_cutoff: score threshold (default no threshold)
	"""
	df = prelim_pipeline(alignment_file, motif_file)
	df.to_csv(os.path.basename(alignment_file) + "_" + os.path.basename(motif_file) + "_bash_output.csv")