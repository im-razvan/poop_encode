# Poop Encode by zeynox

import random

def encode(seed,enc,c_int=2147483647): # Encode Function
    new="";random.seed(seed)
    for letter in enc:
        new+=str(ord(letter)*random.randint(1,c_int))+" "
    return new[:-1]
    
def decode(seed,enc,c_int=2147483647): # Decode Function
    new="";random.seed(seed);enc=enc.split(" ")
    for i in range(len(enc)):
        new += chr(int(int(enc[i])/random.randint(1,c_int)))
    return new
    
"""
Usage:
-> encode(seed,"string to encode") -> encoded_string
-> decode(seed,encoded_string) -> "string to encode"

[!] Bigger seed value = better security.
"""
