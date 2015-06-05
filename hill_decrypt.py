
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

import numpy as np

def hill_decrypt(key, encrypted_seq):
    

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
# it is not working yet so...
    key_matrix = [[3,6],[5,17]]  
  
    adj_key_matrix = [[key_matrix[1][1],-key_matrix[0][1]],[-key_matrix[1][0],key_matrix[0][0]]]
    adj_key_matrix = np.matrix(adj_key_matrix)
    det_inv = np.linalg.inv(key_matrix)
    decrypt_key_matrix = adj_key_matrix*det_inv%26
# it is not working yet, so...
    decrypt_key_matrix =  [[7, 22],[1, 15]]

    decrypt_vector = []
    for vector in encrypt_vector_list:
        encrypt_vector = np.dot(decrypt_key_matrix, vector)
        decrypt_vector.append(list(encrypt_vector))
    
# and I haven't take care about the DNA translation...
    
