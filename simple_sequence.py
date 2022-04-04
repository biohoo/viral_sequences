import Bio
from Bio.Seq import Seq
from Bio.Data import CodonTable


dna = Seq('ATGTGCC')
seq2 = Seq('GGTGGATTAGTA')
result = dna[0:3] + seq2

print(result.transcribe())
print(result.transcribe().translate())
print(dir(CodonTable))

