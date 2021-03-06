from Bio import Align
import configparser
import time
import csv
aligner=Align.PairwiseAligner()
aligner.mode = 'global'
aligner.match_score=2
aligner.mismatch_score = -1
aligner.open_gap_score=-.05
aligner.extend_gap_score=-0.1
config=configparser.ConfigParser()
config.read('config.ini')
query_seq=config['DEFAULT']['pairwise_query_sequence']

f=open("representative_sequences - split_2.FASTA", "r")
# read the query sequence from config
eof=False
# check if readline is empty
results_dict={}
output_file=open("pairwise_scoring.csv","a", newline='')
writer=csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=" ")

while (eof == False):
    line=f.readline()
    desc=""
    full_seq=""
    if line == "":
        eof = True
    else:
        if line[0] == ">" :
            desc=line[1:]
            #change these depending on single or double lines
            seq_line_1=f.readline()
            #seq_line_2=f.readline()
            #full_seq=seq_line_1.strip()+seq_line_2.strip()
            full_seq=seq_line_1.strip()
            aligner=Align.PairwiseAligner()
            aligner.mode = 'global'
            aligner.match_score=2
            aligner.mismatch_score = -1
            aligner.open_gap_score=-.05
            aligner.extend_gap_score=-0.1
            print (desc.strip())
            #print (full_seq)
            for alignment in aligner.align(full_seq, query_seq):
                #print (alignment.score)
                writer.writerow([desc.strip(),alignment.score])
                del aligner
                break
            

# if first character is > then it's a description
#  read another two lines to get the sequence
# pairwise2 compare the query sequence and the read sequence
# list of description and score 
# output list sorted from highest to lowest score

