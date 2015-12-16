import collections
import random
import ast
import json
import os
import numpy as np
'''
Created on Dec 8, 2015

@author: aashishlalani
'''

def Encrypt(string, pad):
    
    stringInBin2 = ''
    for x in string:
        #print x
        temp = ''.join(format(ord(x), 'b'))
        
        while(len(temp) < 8):
            temp = "0" + temp
        
        stringInBin2 = stringInBin2 + (temp);
        
    #print "msgInBin: " + str(stringInBin2)
    #print "lenof msgInBin: " + str(len(stringInBin2))
    #print "pad: " + str(pad)
    res = []
    for i in range (0, len(stringInBin2)):
        #print i
        res.append(int(stringInBin2[i]) ^ pad[i])
    
    #print "res after xoring: " + str(res)
    #print "len of res: " + str((len(res)))
    
    encrypted = ''
    count = 0;
    while (count < len(res)):
        temp = ''
        while(len(temp) < 8 and count < len(res)):
            #print "count" + str(count)
            temp = temp + str(res[count])
            count += 1
        #print temp
        encrypted = encrypted + chr(int(temp, 2))
        temp = ''
    
    #print "encrypted msg: " + str(encrypted)
    return encrypted


#use encrypt for decrypt
def Decrypt(string, pad):
    '''
    res = []
    for i in range(0, len(string)):
        char = string[i]
        for j in range(0, 128):
            if (pad[j] == char):
                res.append(chr(j))
    
    s = ''.join(res)
    '''
    print "starting decrypt!!!! __________________"
    stringInBin2 = ''
    for x in string:
        print x
        temp = ''.join(format(ord(x), 'b'))
        
        while(len(temp) < 8):
            temp = "0" + temp
        
        stringInBin2 = stringInBin2 + (temp);
        
    print "msgInBin: " + str(stringInBin2)
    print "lenof msgInBin: " + str(len(stringInBin2))
    print "pad: " + str(pad)
    return ''
    pass
    
def GenerateKey(msg):
    
    
    
    key = []
    msgInAscii = []
    
    
    stringInBin = ''.join(format(ord(x), 'b') for x in msg)
    
    stringInBin2 = ''
    for x in msg:
        temp = ''.join(format(ord(x), 'b'))
        while(len(temp) < 8):
            temp = "0" + temp
        
        stringInBin2 = stringInBin2 + (temp);
    
    msg_len = len(stringInBin2)
    #print "msg len " + str(msg_len)
    '''
    ascii = {i: chr(i) for i in range(0, 128)}
    keys = list(ascii.keys())
    random.shuffle(keys)
    res = {keys[i]: ascii[i] for i in range(0, 128)}
   
    return res
    '''
    for i in range(0, msg_len):
        key.append(random.SystemRandom().randint(0, 1))

    return key
    pass

def main():

    pad = GenerateKey("Hello hello hello")
    
    res = Encrypt("Hello hello hello", pad)
    deRes = Encrypt(res, pad)
    print res
    print deRes

if __name__ == '__main__':
    main()  