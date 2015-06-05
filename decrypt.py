def mkstr(prefix):
    if len(prefix) == 4:
        return [prefix]
    combs = []
    combs.extend(mkstr(prefix + "A"))
    combs.extend(mkstr(prefix + "T"))
    combs.extend(mkstr(prefix + "G"))
    combs.extend(mkstr(prefix + "C"))
    return combs
 
letters = ""
ATGC_comb = mkstr(letters)
def decrypt(key, genome_encrypted):
    genome_encrypted = list(genome_encrypted)
    encrypt_seq = []
    DNA_letters = []
    
    for chrct in genome_encrypted:
        DNA_letters.append(chrct)
        if len(DNA_letters) ==4:
            DNA_letters = "".join(DNA_letters)
            encrypt_seq.append(DNA_letters)
            DNA_letters = []

    if encrypt_seq[-1] == ATGC_comb[ord('1')]:
        import caesar_decrypt as cd
        return cd.caesar_decrypt(key, encrypted_seq)
    
    elif encrypt_seq[-1] == ATGC_comb[ord('2')]:
        import vigenere_decrypt as vd
        return vd.vigenere_decrypt(key, encrypted_seq)

    elif encrypt_seq[-1] == ATGC_comb[ord('3')]:
        import hill_decrypt as hd
        return hd.hill_decrypt(key, encrypted_seq)
        
    elif encrypt_seq[-1] == ATGC_comb[ord('4')]:
        import AES_decrypt as ad
        return ad.AES_decrypt(key, encrypted_seq)