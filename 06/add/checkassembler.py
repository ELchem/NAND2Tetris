# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:47:38 2019

@author: Dell
"""

f1 = open(r'C:\Users\Dell\Desktop\HDL Nand2Tetris\nand2tetris\projects\06\add\AddHack.hack', 'r')
f2 = open(r'C:\Users\Dell\Desktop\HDL Nand2Tetris\nand2tetris\projects\06\add\Add_correct.hack', 'r')
for line in f1:
    print(line)
for line2 in f2:
    print(line2)
if f1 == f2:
    print('pass')
else:
    print(  'failed' )
    
f1.close()
f2.close()