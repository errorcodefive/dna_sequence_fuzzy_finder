import numpy as np
import configparser
import time
from collections import deque
import csv
# This file will read from config.ini and take the sense, antisense and surrounding nucleotide length
# This file will output all found locations of the sense and antisense series along with the file/chromosome name
# This file will APPEND all found data so make sure there does "found_sequence_sense.csv" and "found_sequence_antisense.csv" does not already exist

# List of .fasta files to go through, I have them named chr1-22, chrx, chry
# Files must be placed in same directory as main.py

chr_list = ["chr1",
    "chr2",
    "chr3",
    "chr4",
    "chr5",
    "chr6",
    "chr7",
    "chr8",
    "chr9",
    "chr10",
    "chr11",
    "chr12",
    "chr13",
    "chr14",
    "chr15",
    "chr16",
    "chr17",
    "chr18",
    "chr19",
    "chr20",
    "chr21",
    "chr22",
    "chrx",
    "chry"
    ]
# Only loading 2 chromosomes during testing

# Load parameters from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
seq=config['DEFAULT']['sequence']
antiseq=config['DEFAULT']['anti_sequence']
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
        line_num =0
        full_pop_size = len(seq)+surround_len*2
        frame_queue = deque([])
        for new_line in infile:
            line_num+=1
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
                    anti_seq_match=True
                    frame_pos = int(surround_len)
                    anti_seq_pos=0
                    while anti_seq_match==True:
                        #Look at specific position
                        if frame_queue[frame_pos] == antiseq[anti_seq_pos]:
                            anti_seq_match = True
                            anti_seq_pos+=1
                            frame_pos+=1
                        else:
                            anti_seq_match = False
                        if(anti_seq_pos==len(antiseq)):
                            # print("Sequence found on line: " + str(line_num)+ ", " + str(total_char-surround_len-len(antiseq))+ ".")
                            anti_seq_match = False
                            # Output position, sense/antisense, chromosome (aka file name), sequence
                            output_seq = ""
                            for j in range(-surround_len, surround_len):
                                output_seq=output_seq+frame_queue[frame_pos+j]
                            with open('found_sequence_anti.csv', mode='a', newline='') as output_file:
                                output_writer = csv.writer(output_file, delimiter=',')
                                output_writer.writerow([(total_char-surround_len-len(seq)+line_num-2), 'antisense', chr, output_seq.strip()])
                            #Save position and surrounding sequences    
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
                            #print("Sequence found on line: " + str(line_num)+ ", " + str(total_char-surround_len-len(seq))+ ".")
                            seq_match = False
                            # Output position, sense/antisense, chromosome (aka file name), sequence
                            output_seq = ""
                            for j in range(-surround_len, surround_len):
                                output_seq=output_seq+frame_queue[frame_pos+j]
                            with open('found_sequence.csv', mode='a', newline='') as output_file:
                                output_writer = csv.writer(output_file, delimiter=',')
                                output_writer.writerow([(total_char-surround_len-len(seq)+line_num-2), 'sense', chr, output_seq.strip()])
                            #Save position and surrounding sequences
        print("Finished and processed " + str(total_char) + " nucleotides.")
# Iterate through every nucleotide and location for sequence

# If sequence is found then note: location, chromosome, +- 50nt sequence

# Write to file as you go in case of errors

# Use GFF after Loci are found to find annotation information
