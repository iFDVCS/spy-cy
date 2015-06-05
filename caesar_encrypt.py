def caesar_encrypt(key, message):
	
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


# modification of the key to get an active key
	key = list(key)
	print key
	act_key  = 0
	for element in key :
		act_key += ord(element)

	encrypt = []
	for chrct in message:
		letter = ATGC_comb[(ord(chrct) + act_key)%256]
		encrypt.append(letter)

		# here I add the restriction site marker
	encrypt.append(ATGC_comb[ord('1')])
	encrypt = ''.join(encrypt)

	return encrypt
