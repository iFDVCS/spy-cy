def find_all(msg, site):
    start = 0
    while site in msg:
        start = msg.find(site, start)
        if start == -1: return
        yield start
        start += len(site) 

def encrypt(key, message, genome, level):

	if level == 1:
		import caesar_encrypt as ce
		encrypt_message = ce.caesar_encrypt(key, message)

	elif level == 2:
		import vigenere_encrypt as ve
		encrypt_message = ve.vigenere_encrypt(key, message)

	elif level == 3:
		import hill_encrypt as he
		encrypt_message = he.hill_encrypt(key, message)

	elif level == 4:
		import AES_encrypt as ae
		encrypt_message = ae.AES_encrypt(key, message)

	return encrypt_message
    print encrypt_message

#	position = find_all(genome_sequence, ATTTTA)
#	print position
