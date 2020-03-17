# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:38:40 2020

@author: Revel
"""
with open('rosalind_DNA.txt', 'r+') as file:
    dna_string = file.read()
    
for letter in ['A', 'C', 'G', 'T']:
    print(dna_string.count(letter), end=' ')