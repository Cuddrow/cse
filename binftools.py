def FastaReader():
    filename = str(input("Input filename: "))
    sequence = open(filename+".fasta", "r")
    DNA_list = sequence.readlines()
    sequence.close()
    DNA_string = ""
    for line in DNA_list[1:]:
        DNA_string += line.strip()

    return DNA_string

def FastaSlicer(slice_sequence, start, finish):
    DNA_sequence = ""
    for index, base in enumerate(slice_sequence):
        if index >= start and index <= finish:
            DNA_sequence += base

    write = str(input("Write to file? "))
    if write == "y" or write == "yes":
        write = True
    else:
        write = False

    if write == True:
        outfilename = str(input("Save as: "))
        outputfile = open(outfilename+".txt", 'w')
        outputfile.write(DNA_sequence)
        outputfile.close()

    return DNA_sequence

def Punnett_Square(parent_1, parent_2):
    import pandas as pd
    table = pd.DataFrame(index=parent_1, columns=parent_2)
    for index_1, allele_1 in enumerate(parent_1):
        for index_2, allele_2 in enumerate(parent_2):
            table.iloc[index_1, index_2] = allele_1 + allele_2

    return table
