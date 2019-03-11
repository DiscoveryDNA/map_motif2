from MSE import *
import sys

def bash_pipeline(alignment_file, motif_file, stand_cutoff=-50):
	"""
	alignment_file: shortened name of alignment file; for example "VT0809.fa"
	motif_file: motif file name, for example "bcd_FlyReg.fm"
	stand_cutoff: score threshold (default no threshold)
	"""
	align_path = "../../TFBS_presence/data/alignments/align_outlier_rm_with_length_" + alignment_file
	motif_path = "../../TFBS_presence/data/pwm/" + motif_file
	df = prelim_pipeline(align_path, motif_path)
	df.to_csv("../data/" + alignment_file[:-3] + "_bash_output")
	# tacks on the alignment file name without ".fa" for the name of the csv output

bash_pipeline(sys.argv[1], sys.argv[2])