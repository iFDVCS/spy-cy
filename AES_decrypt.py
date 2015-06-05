import random
import string
from Crypto import Random
from Crypto.Cipher import AES
import base64

size=16

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

def AES_decrypt(key, encrypted_message):

    decrypt = []
    for chrct in encrypted_message:
        value = ATGC_comb.index(chrct)
        letter = chr(value)
        decrypt.append(letter)

    decrypt_message = ''.join(decrypt)

    act_key = 0
    for element in key:
        act_key += ord(element)

    random.seed(act_key)
    rand_string = ''.join(random.choice(string.ascii_uppercase) for i in range(16))

    iv = Random.new().read(size)
    aes = AES.new(rand_string, AES.MODE_CFB, iv)
    decrypt_message = aes.decrypt(base64.b64decode(decrypt_message))
    return decrypt_message
