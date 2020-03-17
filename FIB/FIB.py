# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:22:38 2020

@author: Revel
"""

n = 30
k = 4
adult_rabbits_pairs = 0
new_adult_rabbits_pairs = 0
baby_rabbits_pairs = 1
for _ in range(n):
    total = baby_rabbits_pairs, new_adult_rabbits_pairs, adult_rabbits_pairs
    print(total, sum(total))
    adult_rabbits_pairs += new_adult_rabbits_pairs
    new_adult_rabbits_pairs = baby_rabbits_pairs
    baby_rabbits_pairs = adult_rabbits_pairs*k
    