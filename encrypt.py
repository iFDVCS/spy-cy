
# DJINA'sfunction, used to find some specficssequences into the genome where we want incorporate
# the message.
def find_all(msg, site):
    start = 0
    while site in msg:
        start = msg.find(site, start)
        if start == -1: return
        yield start
        start += len(site) 

# it is the main function of encryption. It will choose the type of encryption and import the 
# right module to encrypt the message.

def encrypt(message, key, level, genome):

# first cipher, it is working
    if level == 1:
        import caesar_encrypt as ce
        encrypt_message = ce.caesar_encrypt(key, message)

# second cipher, it is not working, I am stuck at the end...
    elif level == 2:
        # I add a problem with global errors, so for this cipher, the key is generating in this module and not in the 
        # vigenere one
        import random
        import vigenere_encrypt as ve
            # get a useful value from the key in order to generate pseudo randomnumber
        act_key = 0
        for chrct in key:
            act_key += ord(chrct)

        random_numbers = []
        random.seed(act_key)

        for i in range(len(message)):
            random_numbers.append(random.randint(1, 255))
    
        encrypt_message = ve.vigenere_encrypt(random_number, message)

# third cipher, it isnot working, I have an input but I don't understand why...
    elif level == 3:
        import hill_encrypt as he
        encrypt_message = he.hill_encrypt(key, message)

# fourth, it is working, but I am using library, it is a little bit cheating.
    elif level == 4:
        import AES_encrypt as ae
        encrypt_message = ae.AES_encrypt(key, message)

# before to encrypt the message we will found where in the genome we will put the message.
# that's why we are searching a specific pattern. 

# fist we find a pattern of a specific sequence. DJINA did a dictionary to have choice but I haven't
# the time to use it. The code is on github. I willuse just a sequence.
    position = find_all(genome, ATTTTA)
    genome_list = list(genome)
    genome_list.insert(position, encrypt_message)

    return encrypt_message
