# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:58:20 2020

@author: Revel
"""
complements = {'C':'G', 'G':'C', 'A':'T', 'T':'A'}
with open('rosalind_revc.txt', 'r+') as file:
    dna_string = file.read().strip('\n')

rc = ''  
for bp in dna_string[::-1]:
    rc += complements[bp]

print(rc)