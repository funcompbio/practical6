f = open("HBB.fa")
line = f.readline()                  ## read the first line from HBB.fa
print("The DNA sequence from gene:")
print(line.strip())                  ## print the first line from HBB.fa

seq = ""                             ## seq will store the whole gene DNA
while (line) :                       ## while 'line' is not empty
    line = f.readline()              ## read the next line from HBB.fa
    seq = seq + line.strip()         ## concatenate that line to 'seq'

v = list(seq)                        ## convert 'seq' into a vector 'v'
n = len(v)                           ## calculate the length of vector 'v'
print(f"has a total of {n} nucleotides")
