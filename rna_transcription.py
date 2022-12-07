def to_rna(dna_strand):
    rna = ""
    for ch in dna_strand:
        if ch == 'A':
            rna = rna + 'U'
        elif ch == 'T':
            rna = rna + 'A'
        elif ch == 'C':
            rna = rna + 'G'
        elif ch == 'G':
            rna = rna + 'C'
    return rna
            
        
