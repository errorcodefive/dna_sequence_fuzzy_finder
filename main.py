import numpy as np
import configparser
import time
from collections import deque

# List of .fasta files to go through, I have them named chr1-22, chrx, chry
# Files must be placed in same directory as main.py
chr_list = ["test"
    ]
# Only loading 2 chromosomes during testing

# Load parameters from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
seq=config['DEFAULT']['sequence']
surround_len=int(config['DEFAULT']['surround_length'])

print ("Sequence: " + seq +". Len: " + str(surround_len))
# Check chromosome files in chr_list are present

for chr in chr_list:
    try:
        f=open(chr+".fasta")
    except FileNotFoundError:
        print("File: " + chr+".fasta"+" not found.")
    finally:
        f.close()
# Iterate through each chromosome

for chr in chr_list:
    # Open chr file
    with open(chr+'.fasta') as infile:
        print("First" + infile.readline())
        
        line_first = ""
        line_last = ""
        line_combined = ""
        total_char = 0
        line_num_char = 0
        full_pop_size = len(seq)+surround_len*2
        frame_queue = deque([])
        for new_line in infile:
            for nuc in new_line.strip():
                total_char +=1
                # If frame_queue is not fully populated
                if len(frame_queue)<full_pop_size:
                    frame_queue.append(nuc)
                else:
                    frame_queue.append(nuc)
                    frame_queue.popleft()
                    # Check for seq
                    seq_match=True
                    frame_pos = int(surround_len)
                    seq_pos = 0
                    while seq_match == True:
                        #Look at specific position
                        if frame_queue[frame_pos] == seq[seq_pos]:
                            seq_match = True
                            seq_pos+=1
                            frame_pos+=1
                        else:
                            seq_match = False
                        if(seq_pos==len(seq)):
                            print("Sequence found at " + str(total_char-surround_len+2-len(seq))+ ".")
                            seq_match = False
                            #Save position and surrounding sequences
        print("Finished and process " + str(total_char) + " nucleotides.")
# Iterate through every nucleotide and location for sequence

# If sequence is found then note: location, chromosome, +- 50nt sequence

# Write to file as you go in case of errors

# Use GFF after Loci are found to find annotation information
