from MSE import *
import os
import sys

def bash_pipeline(alignment_file, motif_file, stand_cutoff=-50):
	"""
	alignment_file: alignment file path
	motif_file: motif file path
	stand_cutoff: score threshold (default no threshold)
	"""
	align_name = os.path.basename(alignment_file)
	motif_name = os.path.basename(motif_file)
	print("Alignment File: ", align_name)
	print("Motif File: ", motif_name)
	print("Threshold: ", stand_cutoff)

	df = prelim_pipeline(alignment_file, motif_file)
	df.to_csv(align_name[-10:] + "_" + motif_name + "_bashoutput.csv")
	print("Success! The outputted CSV file is located at: ", os.getcwd())

# Make sure inputted arguments are valid
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

try:
    alignment = list(SeqIO.parse(arg1, "fasta"))
except:
    print ("ERROR: This is not a fasta alignment file")
    sys.exit()
try:
    motif = motifs.read(open(arg2), "pfm")
except:
    print ("ERROR: This is not a pfm file")
    sys.exit()
try:
    threshold = arg3
except IndexError:
    threshold = -10000

bash_pipeline(arg1, arg2, arg3)