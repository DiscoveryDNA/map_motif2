from MSE import *
import sys

def bash_pipeline(alignment_file, motif_file, stand_cutoff=-50):
	df = prelim_pipeline(alignment_file, motif_file)
	df.to_csv("../data/trial")

bash_pipeline(sys.argv[1], sys.argv[2])