DNA = "GCTA"
RNA = "CGAU"

def to_rna(dna_strand):
    dna_to_rna = dict(zip(DNA,RNA))
    return "".join([ dna_to_rna.get(nuc) for nuc in dna_strand])
