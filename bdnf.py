sequence = open("homobdnf.fasta", "r")
lines = sequence.readlines()
sequence.close()


dots = ""
for line in lines[1:]:
    dots += line.strip()

#print (dots)
#print(type(dots))

pcr_sequence = ""
for index, base in enumerate(dots):
    if index >= 63617 and index <= 63787:
        pcr_sequence += base
        #print (index - 63617)

print (pcr_sequence)
print(len(pcr_sequence))
print(len(dots))

outputfile = open("bdnfpcrseq.txt", 'w')
outputfile.write(pcr_sequence)
outputfile.close()
