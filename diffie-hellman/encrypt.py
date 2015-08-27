from dh import diffie_hellman
import sys
from random import choice
from base64 import b64encode
from base64 import b64decode

"""
Use simple diffie-hellman to encrypt a message using 
repeating-key XOR (DH secret -> bytearray)

We use the DH secret to generate an 2-byte array
since the maximum value for the secret is 1000
(1000.bit_length() == 10, so two bytes is plenty)
"""

class DHExample(object):
    def __init__(self, plaintext):
        self.plaintext = plaintext
        self.mod = choice(range(1000))
        self.base = choice(range(1000))
        self.secret = diffie_hellman(self.mod, self.base, True)
        self.key = self.secret.to_bytes(2, sys.byteorder)
        self.ciphertext = ''

    def encrypt(self):
        print("Alice encrypts her message to Bob. They share")
        print("the DH key {}.\n".format(self.secret))

        plain_bytes = bytearray(self.plaintext, 'ascii')
        ciphertext = bytearray()
        for i in enumerate(self.plaintext):
            ciphertext.append(ord(i[1]) ^ self.key[i[0] % len(self.key)])
        self.ciphertext = b64encode(ciphertext)

        print("Alice XORs the message: {}".format(self.plaintext))
        print("She produces the ciphertext: {}\n".format(self.ciphertext))

    def decrypt(self):
        print("Bob wants to decrypt the message. He performs the same")
        print("operation as Alice, using their shared secret")

        plain_bytes = bytearray()
        ciphertext = b64decode(self.ciphertext)
        for i in enumerate(ciphertext):
            plain_bytes.append(i[1] ^ self.key[i[0] % len(self.key)])
        plaintext = ''.join(map(chr, plain_bytes))

        print("Bob decrypts the ciphertext to:")
        print(plaintext)

if __name__ == '__main__':
    dh = DHExample('Wow, encryption! What a thing! DH to generate secrets!')
    dh.encrypt()
    dh.decrypt()
