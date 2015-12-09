import collections
import random
import ast
import json
'''
Created on Dec 8, 2015

@author: aashishlalani
'''

def Encrypt(string, pad):
    print string + "CRAZY"
    res = []
    for i in range (0, len(string)-1):
        print ord(string[i]) 
        res.append(pad[ord(string[i])])
    
    s = ''.join(res)
    print s
    return s

def Decrypt(string, pad):
    res = []
    for i in range(0, len(string)):
        char = string[i]
        for j in range(0, 128):
            if (pad[j] == char):
                res.append(chr(j))
    
    s = ''.join(res)
    return s
    pass
    
def GenerateKey():
    ascii = {i: chr(i) for i in range(0, 128)}
    keys = list(ascii.keys())
    random.shuffle(keys)
    res = {keys[i]: ascii[i] for i in range(0, 128)}
   
    return res
    pass

def main():
    pad = GenerateKey()
    res = Encrypt("HELLO HELLO HELLO MY NAME IS AASHISN", pad)
    deRes = Decrypt(res, pad)
    print res
    print deRes

if __name__ == '__main__':
    main()  