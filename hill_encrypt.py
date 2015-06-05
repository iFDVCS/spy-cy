# Omar solution for our combinatory problem
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

# this cipher, called Hill cipher, use matrix to do substitution of characters values.
# my main references are the hill cipher wikipedia page (that is explaining what are the numerical operations
# needed to encrypt the message) and the numpy.matrix list of functions.
import numpy as np

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
# creation of the encooding matrice with the key!

    key_matrix= []
    i = 0
    for blabla in key:
    
        if len(key_matrix) < 4:
            print key_matrix
            key_matrix.append(ord(key[i]))
            i += 1
        elif len(key_matrix)%4 == 0:
            i = 0
        else:
            key_matrix[i] = (key_matrix[i] + ord(key[i]))
            i += 1
# it is not working yet
    A = [[3,6],[5,17]]

    encrypt_vector_list = []

# matrix multiplication 
    for vector in no_crypt_vector_list:
        encrypt_vector = np.dot(A, vector)
        encrypt_vector_list.append(list(encrypt_vector))
    encrypt_vector_list = [[sum(encrypt_vector_list[0]),sum(encrypt_vector_list[1])],[sum(encrypt_vector_list[2]),sum(encrypt_vector_list[3])]]

    
    DNA_message = []
    for vector in encrypt_vector_list:
        for value in vector:
            DNA_message.append(ATGC_comb[value])
            
    # here I should add the restriction site marker
    DNA_message.append(ATGC_comb[ord('3')])
    DNA_message = "".join(DNA_message)
