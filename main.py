import numpy as np
import configparser

# List of .fasta files to go through, I have them named chr1-22, chrx, chry
# Files must be placed in same directory as main.py
chr_list = [
    "chr1", 
    "chr2"
    ]
# Only loading 2 chromosomes during testing

# Load parameters from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
seq=config['DEFAULT']['sequence']
surround_len=config['DEFAULT']['surround_length']

print ("Sequence: " + seq +". Len: " + surround_len)
# Check chromosome files in chr_list are present

for chr in chr_list:
    try:
        f=open(chr+".fasta")
    except FileNotFoundError:
        print("File: " + chr+".fasta"+" not found.")
    finally:
        f.close()
# Iterate through each chromosome

# Iterate through every nucleotide and location for sequence

# If sequence is found then note: location, chromosome, +- 50nt sequence

# Write to file as you go in case of errors

# Use GFF after Loci are found to find annotation information
