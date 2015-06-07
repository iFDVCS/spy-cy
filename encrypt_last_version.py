# It is working !! On ipython I can encrypt all the files and input them into a genome.
# But it is not working with the interface, I can see markers of encryption and the genome but I cannot see
# the encrypt message : why ??? I will find a solution...


import random
import string
import numpy as np
from Crypto import Random
from Crypto.Cipher import AES
import base64

# list of ATGC combinaisons that it used to translate message into DNA sequence
def mkstr(prefix, nbr):
	if len(prefix) == nbr:
		return [prefix]
	combs = []
	combs.extend(mkstr(prefix + "A", nbr))
	combs.extend(mkstr(prefix + "T", nbr))
	combs.extend(mkstr(prefix + "G", nbr))
	combs.extend(mkstr(prefix + "C", nbr))
	return combs
 
letters = ""
ATGC_comb = mkstr(letters, 4)

# It is a simple substitution cipher, the key generate a number between 1 and 256 (I need to check that I never have 0)
# and they use always the same number to shift the letters.

def caesar_encrypt(key, message):

# modification of the key to get an active key
	key = list(key)
	act_key  = 0
	for element in key :
		act_key += ord(element)
        
# encryption of the message and translation into DNA (in the same time)
	encrypt_message = []
	for chrct in message:
		letter = ATGC_comb[(ord(chrct) + act_key)%256]
		encrypt_message.append(letter)

		# here I should add the restriction site marker
	encrypt_message.append(ATGC_comb[ord('1')])
	encrypt_message = ''.join(encrypt_message)

	return encrypt_message

# vigenere is a substitution cipher, as caesar, but here the substitution changeeach time, following some pseudo
# random numbers. Historically, Vigenère built all the different alphabet permutations and they were following in 
# a specific order generate by the key. So here it is almost the same.

def vigenere_encrypt(key, message):

         # get a useful value from the key in order to generate pseudo randomnumber
    act_key = 0
    for chrct in key:
        act_key += ord(chrct)
        
    random_numbers = []
    random.seed(act_key)

    for i in range(len(message)):
        random_numbers.append(random.randint(1, 255))    

    encrypt = []
    i = 0
    for chrct in message:
        letter = ATGC_comb[((ord(chrct) + random_numbers[i])%256)]
        encrypt.append(letter)
        i += 1
    encrypt.append(ATGC_comb[ord('2')])
    encrypt = ''.join(encrypt)
    return encrypt

def hill_encrypt(key, message):
    
# I am converting each character into its value (minus 32 because it is ascii code and it needed
# when you want build a Hill cipher). So each character values is going into a list called vector, when this vector 
# is with to characters, it added into a new list called no_crypt_vector_list. We will use this last
# list to do matrice multiplication with the key and to obtain the encoded value of characters.
    no_crypt_vector_list = []
    vector = []
    for charact in message:
        charact_value = ord(charact)-32
        vector.append(charact_value)
        if len(vector) == 2:
            no_crypt_vector_list.append(vector)
            vector = []
            
# creation of the encoding matrice with the key!

    key_matrix= []
    i = 0
    for blabla in key:
    
        if len(key_matrix) < 4:
            key_matrix.append(ord(key[i]))
            i += 1
        elif len(key_matrix)%4 == 0:
            i = 0
        else:
            key_matrix[i] = (key_matrix[i] + ord(key[i]))
            i += 1
# it is not working yet, actually I am not sure anymore, I should test.
    A = [[3,6],[5,17]]

    encrypt_vector_list = []

# matrix multiplication (= encryption)
    for vector in no_crypt_vector_list:
        encrypt_vector = np.dot(A, vector)
        encrypt_vector_list.append(list(encrypt_vector))
    # Here I generate another list of ATGC combinaisons with 6 letters because this type of encryption needs
    # more combinaison than others (because we have combinaison of letters).
    letters = ""
    ATGC_comb2 = mkstr(letters, 6)
    DNA_message = []
    for vector in encrypt_vector_list:
        for value in vector:
            DNA_message.append(ATGC_comb2[value])
    DNA_message = "".join(DNA_message)
    
    return DNA_message

# definition of the Advanced Encryption Standard. I use functions from Crypto.
def AES_encrypt(key, message):
    size = 16
    act_key = 0
    for element in key:
        act_key += ord(element)

    random.seed(act_key)
    rand_string = ''.join(random.choice(string.ascii_uppercase) for i in range(16))
    iv = Random.new().read(size)
    aes = AES.new(rand_string, AES.MODE_CFB, iv)
    b = base64.b64encode(aes.encrypt(message))

    encrypt = []
    i = 0
    for chrct in b:
        letter = ATGC_comb[ord(chrct)]
        encrypt.append(letter)
        i += 1
    encrypt.append(ATGC_comb[ord('4')])
    encrypt = ''.join(encrypt)
    return encrypt


# encryption function that need to be call.
def encrypt(message, key, level, genome, encrypt_message =""):
    
    # first cipher, it is working
    if level == 1:
        encrypt_message = caesar_encrypt(key, message)
    
    # second cipher, it is not working, I am stuck at the end...
    elif level == 2:
        encrypt_message = vigenere_encrypt(key, message)        
        
    # third cipher, it is not working,
    elif level == 3:
        encrypt_message = hill_encrypt(key, message)
                
    # fourth, it is working, but I am using library, it is a little bit cheating.
    elif level == 4:
        encrypt_message = AES_encrypt(key, message)
    
    #return encrypt_message

# before to encrypt the message we will found where in the genome we will put the message.
# that's why we are searching a specific pattern. 
    if genome != '':
# fist we find a pattern of a specific sequence. DJINA did a dictionary to have choice but I haven't
# the time to use it. The code is on github. I willuse just a sequence.
        restrict_site = 'GATTTTAC'
        position = genome.find(restrict_site, 0)
        #genome = string.upper(genome)
        genome_list = list(genome)
        
        # I have a doubt, maybe it delete the restrict_site or it put the message before. I need to check.
        genome_list.insert(position, encrypt_message)
        genome_list.insert((position + len(encrypt_message)), restrict_site)
        genome_list.append(restrict_site)
        return "".join(genome_list)
    else:
        encrypt_message = encrypt_message + "AAAAAAAA"
        #encrypt_message = "".join(encrypt_message)
        return encrypt_message
        

