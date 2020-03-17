# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:56:41 2020

@author: Revel
"""
def countGC(string):
   return string.count('G')+string.count('C') 

candidates = {}
name = ''

with open('rosalind_GC.txt', 'r+') as file:
    a = list(file)
    for each_line in a:
        if each_line.startswith('>'):
            name = each_line.strip('\n')
            sequence= ''
            candidates[name] = sequence
        else:
            candidates[name] += each_line.replace("\n", "")

for name, seq in candidates.items():
    candidates[name]= 100*countGC(seq)/len(seq)

print(candidates)
highest = max(candidates, key=candidates.get)
print(highest[1:])
print(candidates[highest])