# list of DNA combinaisons.
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

# DJINA's function, used to find some specfics sequences into the genome where we incorporated
# the message.
def find_all(msg, site):
    start = 0
    while site in msg:
        start = msg.find(site, start)
        if start == -1: return
        yield start
        start += len(site) 

# decryption function. It call other functions in order to decrypt the differents types of encryption. 
def decrypt(key, genome_encrypted):
    
    # first we have a genome and we need to find where is our message.
    # At the end of the message we can find the restriction site that we will search to know where start and finish
    # our message.
    list_genome_encrypted = list(genome_encrypted)
    list_genome_encrypted2 = []
    message_encrypted = []
    restrict_site = []
    for i in range(8):
        a = -(i+1)
        restrict_site.append(a)
    if restrict_site != 'AAAAAAAA':
        position = find_all(restrict_site, genome_encrypted)
        position = list(position)
        if position != []:
            first_site = position[0]
            second_site = position[1]
    # We found the two sites around our sequence, so we will keep the sequence between.
            for i in range(second_site):
                list_genome_encrypted2.append(i)
            for i in range(first_site):
                list_genome_encrypted2.pop(i)
            message_encrypted = list_genome_encrypted2
            
    # if it is a sequence encrypted without genome:
    else:
        for i in range(8):
            message_encrypted = list_genome_encrypted.pop(-1) 

    
    encrypt_seq = []
    DNA_letters = []  
    for chrct in message_encrypted:
        DNA_letters.append(chrct)
        if len(DNA_letters) ==4:
            DNA_letters = "".join(DNA_letters)
            encrypt_seq.append(DNA_letters)
            DNA_letters = []

    if DNA_letters == ATGC_comb[ord('1')]:
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
