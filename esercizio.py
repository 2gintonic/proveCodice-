import csv

with open('csv.csv','r') as inputfile, open('output.txt','w') as outputfile:
    reader = csv.reader(inputfile)

righecounter = 0
for righe in reader:
    righecounter += 1
    outputfile.write(righecounter)