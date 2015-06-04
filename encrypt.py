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
		import rossignol_encrypt as re
		encrypt_message = re.rossignol_encrypt(key, message)

	elif level == 5:
		import linear_encrypt as le
		encrypt_message = le.linear_encrypt(key, message)

	return encrypt_message


	with open(genome) as genome_file:
		genome_sequence = genome_file.read()


	position = find_all(genome_sequence, ATTTTA)
	print position

# I haven't finish here (I am waiting for Djina's loop. Doesn't matter you can run the code
	# ajoute encrypt_message position 63, à la fin du message on ajoute la sequence
	# qu'on doit verifier et le niveau d'encryption.


# input variable to test the code without connection with the interface	
print " a key please"
key = raw_input()

print "position of your message"
message = raw_input()

print "position of your genome sequence"
genome =raw_input()

print"level of encryption"
level = input()

encrypt_message = encrypt(key, message, genome, level)
