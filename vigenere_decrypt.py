def vigenere_decrypt(key, encrypted_message):

# get a useful value from the key in order to generate pseudo randomnumber
	act_key = 0
	for chrct in key:
		act_key += ord(chrct)
	# generating a list of pseudo randum number to change thekey value for each characters
	#that we will encode.
	random_numbers = []
    random.seed(act_key)
	for i in range(len(message)):
		random_numbers.append(random.randint(1, 255))

# encryption of the text using permutation of letter. (useless because we change the alphabet, it is not more encrypt
# than just change alphabet to DNA)
	decrypt = []
	i = 0
	for chrct in encrypted_message:
		value = ATGC_comb.index(chrct)
		letter = chr(value%256 - random_number[i])
		i += 1
		decrypt.append(letter)

	decrypt = ''.join(decrypt)
	print decrypt

	#decrypt_file_name = raw_input()
	#decrypt_file = open(decrypt_file_name, "w")
	#decrypt_file.write(decrypt)
	#decrypt_file.close()
	return decrypt
