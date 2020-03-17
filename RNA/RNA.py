# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:54:59 2020

@author: Revel
"""

with open('rosalind_rna.txt', 'r+') as file:
    dna_string = file.read()
    
def transcribe(dna):
    return dna.replace('T', 'U')

print(transcribe(dna_string))