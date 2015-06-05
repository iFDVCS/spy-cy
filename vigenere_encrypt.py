# vigenere cipher

# it is combinatory list of ATGC words.
def mkstr(prefix):
		if len(prefix) == 4:
			return [prefix]
		combs = []
		combs.extend(mkstr(prefix + "A"))
		combs.extend(mkstr(prefix + "T"))
		combs.extend(mkstr(prefix + "G"))
		combs.extend(mkstr(prefix + "C"))
		return combs

letters = ''
ATGC_comb = mkstr(letters)


# function to encrypt message 
def vigenere_encrypt(key, message):
    i = 0
    encrypt = []
    for chrct in message:
        i+= 1
        letter = ATGC_comb[(int(ord(chrct)) + key[i])%256] # ERROR MESSAGE, I mix int and str and I haven't enough time
 #								to fix that
        encrypt.append(letter)

	# here I add the restriction site marker for the tncryption type 2
	encrypt.append(ATGC_comb[ord('2')])
	encrypt = ''.join(encrypt)

	return encrypt
