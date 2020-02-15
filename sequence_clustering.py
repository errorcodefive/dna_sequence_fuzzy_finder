# This file will take the sequences from "found_sequences.csv" and cluster them with a fuzzy c-means algorithm (https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_cmeans.html)
# This file will output all clustered sequences into files labelled ________________
import numpy as np
import skfuzzy as fuzz
import csv
import configparser

# Read config.ini and read sequence and get length
# Read config.ini and get surrounding length
config = configparser.ConfigParser()
config.read('config.ini')
seq_length=len(config['DEFAULT']['sequence'])
surround_len=int(config['DEFAULT']['surround_length'])

read_data = []
# Read in file from found_sequence.csv
with open('found_sequence.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        # Ignore all columns except for 3 (sequence)
        cropped_input = row[3][:surround_len]+row[3][surround_len+seq_length:]
        # For each line that is read in delete the middle portion (the sequence)
        # Load each line into a np array as a series of chars eg [[a,t,g,c],[g,t,c,a]]
        line_np = np.array(list(cropped_input))
        read_data.append(line_np)
np_data = np.array(read_data)
print(np_data)