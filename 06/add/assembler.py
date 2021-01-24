# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:23:53 2019

@author: Dell
"""
import math

def NtoBinary(N):
    binaryRep = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    while N > 0:
        i = int(math.log2(N))
        binaryRep[i] = '1'
        N = N - (2**i)
    binaryRep.reverse()
    return ''.join(binaryRep) 


def convert(line):
    line = line.replace(' ', '')
    line = line.replace('\n','')
    binary = [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if line[1] == ';':
        jline = line.split(';')
        if jline[1] == 'JGT'
    else:    
        ADM = line.split('=')
        if 'D' in ADM[0]:
            binary[11] = 1
        if 'A' in ADM[0]:
            binary[10] = 1
        if 'M' in ADM[0]:
            binary[12] = 1
        if 'M' in ADM[1]:
            binary[3] = 1
        if ADM[1] == '0':
            binary[4:10] = [1,0,1,0,1,0]
        elif ADM[1] == '1':
            binary[4:10] = [1,1,1,1,1,1]
        elif ADM[1] == '-1':
            binary[4:10] = [1,1,1,0,1,0]
        elif ADM[1] == 'D':
            binary[4:10] = [0,0,1,1,0,0]
        elif ADM[1] == 'A' or ADM[1] =='M':
            binary[4:10] = [1,1,0,0,0,0]
        elif ADM[1] == '!D':
            binary[4:10] = [0,0,1,1,0,1]
        elif ADM[1] == '!A' or ADM[1] =='!M':
            binary[4:10] = [1,1,0,0,0,1]
        elif ADM[1] == '-D':
            binary[4:10] = [0,0,1,1,1,1]
        elif ADM[1] == '-A' or ADM[1] =='-M':
            binary[4:10] = [1,1,0,0,1,1]
        elif ADM[1] == 'D+1' or ADM[1] =='1+D':
            binary[4:10] = [0,1,1,1,1,1]
        elif ADM[1] == 'A+1' or ADM[1] =='1+A' or ADM[1] =='M+1' or ADM[1] =='1+M':
            binary[4:10] = [1,1,0,1,1,1]
        elif ADM[1] == 'D-1' or ADM[1] =='-1+D':
            binary[4:10] = [0,0,1,1,1,0]
        elif ADM[1] == 'A-1' or ADM[1] =='-1+A' or ADM[1] =='M-1' or ADM[1] =='-1+M':
            binary[4:10] = [1,1,0,0,1,0]    
        elif ADM[1] == 'D+A' or ADM[1] =='A+D' or ADM[1] =='D+M' or ADM[1] =='M+D':
            binary[4:10] = [0,0,0,0,1,0]
        elif ADM[1] == 'D-A' or ADM[1] =='-A+D' or ADM[1] =='D-M' or ADM[1] =='-M+D':
            binary[4:10] = [0,1,0,0,1,1]
        elif ADM[1] == 'A-D' or ADM[1] =='-D+A' or ADM[1] =='M-D' or ADM[1] =='-D+M':
            binary[4:10] = [0,0,0,1,1,1]
        elif ADM[1] == 'D&A' or ADM[1] =='A&D' or ADM[1] =='D&M' or ADM[1] =='M&D':
            binary[4:10] = [0,0,0,0,0,0]
        elif ADM[1] == 'A|D' or ADM[1] =='D|A' or ADM[1] =='M|D' or ADM[1] =='D|M':
            binary[4:10] = [0,1,0,1,0,1]
    for x,y in enumerate(binary):
        binary[x] = str(y)
    return ''.join(binary)
    
newFile = 'AddHack.hack'
variableCount = 16
HackBinary = []

f1 = open(r'C:\Users\Dell\Desktop\HDL Nand2Tetris\nand2tetris\projects\06\add\Add.asm', 'r')

for line in f1:
    if line[0:2] == '//' or line[0:2] == '\n':
        continue
    elif line[0] == '@':
        if line[1].isdigit():
#            print(line)
            N = NtoBinary(int(line[1::]))
            HackBinary.append(N)
        else:
#            print(line)
            HackBinary.append(NtoBinary(variableCount))
            variableCount += 1
    else:
        lineBi = convert(line)
        HackBinary.append(lineBi)

f1.close()

f2 = open(newFile,'w')
for Line_bi in HackBinary:
    f2.write(Line_bi)
    f2.write('\n')
f2.close()


