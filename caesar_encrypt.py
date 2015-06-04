def caesar_encrypt(key, message):
	def mkstr(prefix):
    	if len(prefix) == 5:
        	return [prefix]
    	
    	combs = []
    	combs.extend(mkstr(prefix + "A"))
    	combs.extend(mkstr(prefix + "T"))
    	combs.extend(mkstr(prefix + "G"))
    	combs.extend(mkstr(prefix + "C"))
    	return combs
 
	letters = ""
	ATGC_comb = mkstr(letters)

	with open(rmessage) as text_file:
    	no_crypt = list(text_file.read())

# enter the key

	#key = raw_input()

# modification of the key to get an active key
	key = list(key)
	print key
	a  = 0
	for element in key :
    	a += ord(element)
	print a

# encryption of the text using permutation of letter. (useless because we change the alphabet, it is not more encrypt
# than just change alphabet to DNA)
	encrypt = []
	for chrct in no_crypt:
    	letter = ATGC_comb[ord(chrct) + a]
    	encrypt.append(letter)

	encrypt = ''.join(encrypt)

	#crypt_file_name = raw_input()
	#crypt_file = open(crypt_file_name, "w")
	#crypt_file.write(encrypt)
	#crypt_file.close()
	return encrypt
