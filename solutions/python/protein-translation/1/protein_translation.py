
STOP_CODON = "STOP"
CODON_DIC = {
	"AUG": 	"Methionine",
	"UUU":  "Phenylalanine",
	"UUC":  "Phenylalanine",
	"UUA":  "Leucine",
	"UUG":  "Leucine",
	"UCU":  "Serine",
	"UCC":  "Serine",
	"UCA":  "Serine",
	"UCG":  "Serine",
	"UAU":  "Tyrosine",
	"UAC":  "Tyrosine",
	"UGU":  "Cysteine",
	"UGC":  "Cysteine",
	"UGG":  "Tryptophan",
	"UAA":  STOP_CODON,
	"UAG":  STOP_CODON,
	"UGA":  STOP_CODON,
}

def proteins(strand):
    output = []
    for idx in range(0,len(strand),3):
       codon = strand[idx:idx+3] 
       if CODON_DIC[codon] == STOP_CODON:
           break
       else:    
           output.append(CODON_DIC[codon])    
    return output    
