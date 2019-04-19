# Map Motif 2

## About
This repository contains a Python package, named map_motif2, which maps transcription factor binding sites (TFBS) onto alignments. There are 3 components of the code, located inside the /map_motif2_code directory:

1. motif_pipeline.py
* INPUT: This script can be run directly from command line. It takes in an alignment file path, a motif file path, and a desired threshold.
* OUTPUT: Generates a CSV file with information about each TFBS: the score, species, raw position, alignment position, and motif associated with it.

2. threshold_setter.py
* Helper script that is imported in motif_pipeline.py. Helps set an appropriate score threshold for determining TFBS's, depending on the motif being used.

3. MSE.py
* Helper script that is imported in motif_pipeline.py. This file, along with threshold_setter.py, are integrated into the final motif_pipeline.py.

## Motivation
The motivation behind mapping TFBS's onto alignments is to eventually gain an understanding of how the presence of TFBS's fluctuates across different species throughout time.

## Features
* map_motif2_code contains a folder for code-testing purposes (currently empty, but can be implemented).

## Usage
Users should run this package through motif_pipeline.py. For example, assuming you are currently inside the map_mptif2/map_motif2_code directory, you may type something like:

python motif_pipeline.py "../../TFBS_presence/data/alignments/align_outlier_rm_with_length_VT0809.fa" "../../TFBS_presence/data/pwm/bcd_FlyReg.fm" -50

in command line. Once the CSV is generated within the same folder, you will see a success message.



