
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

def caesar_decrypt(key, encrypted_message):

# modification of the key to get an active key
	key = list(key)
	print key
	act_key  = 0
	for element in key :
		act_key += ord(element)

# encryption of the text using permutation of letter. 
	decrypt = []
	for chrct in encrypted_message:
		value = ATGC_comb.index(chrct)
		letter = chr(value%256 - act_key)
		decrypt.append(letter)

	decrypt = ''.join(decrypt)
	print decrypt

	#decrypt_file_name = raw_input()
	#decrypt_file = open(decrypt_file_name, "w")
	#decrypt_file.write(decrypt)
	#decrypt_file.close()
	return decrypt
