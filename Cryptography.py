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
def Encrypt(string, pad, start = 0):
    
    stringInBin2 = ''
    for x in string:
        temp = ''.join(format(ord(x), 'b'))
        while(len(temp) < 8):
            temp = "0" + temp
        stringInBin2 = stringInBin2 + (temp);
        
    res = []
    nextStartPoint = 0;
    for i in range (0, len(stringInBin2)):
        res.append(int(stringInBin2[i]) ^ pad[(i + start) % len(pad)])
        nextStartPoint = (i + start) % len(pad) + 1
    
    encrypted = ''
    count = 0;
    while (count < len(res)):
        temp = ''
        while(len(temp) < 8 and count < len(res)):
            temp = temp + str(res[count])
            count += 1
        encrypted = encrypted + chr(int(temp, 2))
        temp = ''
    
    return [encrypted, nextStartPoint]

    
def GenerateKey(pad_len = 1000):
    key = []
    for i in range(0, pad_len):
        key.append(random.SystemRandom().randint(0, 1))

    return key
    pass


def outputPad(filename, pad):
    with open(filename, 'w') as jsonfile:
        json.dump(pad, jsonfile)
    
def inputPad(filename):
    json_res = []
    with open(filename) as jsonfile:
        if (jsonfile is None):
            raise Exception("No such file.")
        try:
            json_res = json.load(jsonfile)
        except ValueError:
            raise Exception('Invalid JSON.')
    return json_res

def main():

    pad = GenerateKey();
    
    input = inputPad("padOutput");
    
    print input;
    
    resAndStartPoint = Encrypt("Hello hello hello", input, 2)
    print resAndStartPoint[1]
    resAndStartPoint2 = Encrypt("SUP SUP SUP", input, resAndStartPoint[1])
    deRes = Encrypt(resAndStartPoint[0], input, 2)
    deRes2 = Encrypt(resAndStartPoint2[0], input, deRes[1]);
    print resAndStartPoint[0]
    print resAndStartPoint2[0]
    print deRes[0]
    print deRes2[0]

if __name__ == '__main__':
    main()  