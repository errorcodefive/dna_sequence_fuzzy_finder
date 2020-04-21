import csv
import time
with open('GRCh38_latest_genomic.gff', newline='') as gffFile:
    gff_reader=csv.reader(gffFile, delimiter='\t')
    for line in gff_reader:
        if line[0][0]!="#":
            fileName="split_gff/"+line[2]+".csv"
            print (fileName)
            with open(fileName, 'a', newline='') as outputFile:
                outFile =csv.writer(outputFile, delimiter=',')
                outFile.writerow(line)
            #open up file with file name line[2].csv
            #output whole line as csv
