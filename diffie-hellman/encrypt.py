from dh import diffie_hellman
from random import choice

"""
Use simple diffie-hellman to encrypt a message using 
single-byte XOR
"""

class DHEncrypt(object):
    def __init__(self, plaintext):
        self.plaintext = plaintext
        self.mod = choice(1000)
        self.base = choice(1000)
        self.secret = diffie_hellman(mod, base, True)
        self.ciphertext = ''

    def encrypt(self):
        print("Alice encrypts her message to Bob. They share")
        print("the DH key {}".format(self.secret))

        plain_bytes = bytearray(plaintext, 'ascii')
        ciphertext = 

