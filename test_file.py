# Omar solution for our combinatory problem
def mkstr(prefix):
    if len(prefix) == 5:
        return [prefix]
    combs = []
    combs.extend(mkstr(prefix + "A"))
    combs.extend(mkstr(prefix + "T"))
    combs.extend(mkstr(prefix + "G"))
    combs.extend(mkstr(prefix + "C"))
    return combs

# generation of 1024 combinaisons of ATGC 
letters = ""
ATGC_comb = mkstr(letters)

# opening the file to read
# put the position and the name of the file like :
# "/Users/Anna/Documents/iFDV/computer science/text_to_code.txt"
with open(input()) as text_file:
    no_crypt = list(text_file.read())

# no encryption here, only translation to DNA
encrypt = []
for chrct in no_crypt:
    letter = ATGC_comb[ord(chrct)]
    encrypt.append(letter)

encrypt = ''.join(encrypt)

# now, we save  the DNAsequence/message:
# first choose the name of the file       We need to add that to the interface ?
crypt_file_name = raw_input()
crypt_file = open(crypt_file_name, "w")
crypt_file.write(encrypt)
crypt_file.close()

