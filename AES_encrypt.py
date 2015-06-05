# for this cipher I used crypto library to import the AES algorithm.

import random
import string
from Crypto import Random
from Crypto.Cipher import AES
import base64

size =16

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

def AES_encrypt(key, message):

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
