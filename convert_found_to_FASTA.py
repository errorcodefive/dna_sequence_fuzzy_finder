import csv
# convert the found_sequence files to a separate .FASTA sequence
# 80 Character width
# ">" before description line, use the sequence nucleotide number, sense/antisense and file name in description

#load found_sequence_anti_fixed
#load found_sequence
# Create output file
output_file = open("converted_fasta.FASTA","a")


with open('found_sequence_anti_fixed.csv', 'r') as antiFile:
    reader = csv.reader(antiFile, delimiter=",")
    for row in reader:
        desc = ">"+row[0]+","+row[1]+","+row[2]+"\n"
        output_file.write(desc)
        seq=row[3][0:79]+"\n"+row[3][79:]+"\n"
        output_file.write(seq)
# While not eol -> get line
with open('found_sequence.csv', 'r') as File:
    reader2 = csv.reader(File, delimiter=",")
    for row in reader2:
        desc = ">"+row[0]+","+row[1]+","+row[2]+"\n"
        output_file.write(desc)
        seq=row[3][0:79]+"\n"+row[3][79:]+"\n"
        output_file.write(seq)