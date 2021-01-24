# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:09:56 2019

@author: Dell
"""

## writing hdl chips
f1 =  open('PC.hdl','r+')
And_hdl = f1.readlines()

bits = 16

for x,line in enumerate(And_hdl):
    if line == '//*\n':
        orig_code ='//'.join(And_hdl[x+1:-1]) 
        parts = ''.join(And_hdl[x+1:-1])
        break
print(orig_code)
print(parts)
del And_hdl[x+1:-1]
for y in range(1,bits):
    temp_str = parts.replace('?',str(y))
    temp_str2 = temp_str.replace('%',str(y-1))
    And_hdl.insert(x+y,temp_str2)
  
#clear the text file
f1.truncate(0)   

#f1.writelines('// ' + orig_code)
print(And_hdl)
orig_code_b = '// ' + orig_code
And_hdl.insert(0, orig_code_b)
print(And_hdl)
f1.writelines(And_hdl)
#f1 =  open('Mux8Way16.hdl','r+')
#find_296 = f1.readlines()
#print(find_296[295])
f1.close()    
    
