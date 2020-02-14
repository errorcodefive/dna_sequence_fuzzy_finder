# This flips the antisense so that it reads 3' to 5' and inverts so that the sense is obtained
import time
import csv

nucleotide_complements = {
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G",
    "N":"N"
}

with open("found_sequence_anti.csv")  as infile:
    #read as csv
    csv_reader = csv.reader(infile, delimiter =",")
    for row in csv_reader:
        try:
            seq_in = row[3]
            seq_reversed = str(seq_in[::-1])
            print("Reversed: " + seq_reversed)
            seq_complement=""
            for nuc in seq_reversed:
                seq_complement+=nucleotide_complements[nuc]
            with open('found_sequence_anti_fixed.csv', mode='a') as output_file:
                output_writer = csv.writer(output_file, delimiter = ',')
                output_writer.writerow([row[0], row[1], row[2], seq_complement])
        except IndexError:
            pass

print("Done")