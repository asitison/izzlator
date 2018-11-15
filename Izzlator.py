# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:37:09 2018

@author: asiti
"""
# Somebody had to do it...
#======== THE IZZLATOR! ========================
print("\n\n")
print("------------")
print("THE ISSLATOR")
print("------------\n")
n = 2
phrase = {}

vizzle = "izzle"
i = -1
phrase = input("What should I IZZLE for you? ")
words = phrase.split()
wlen = len(words)
for word in words:
     i += 1
     if len(word) > 4:
         n = int(len(word)/2)
         if (word[1] in ['a','e','i','o','u']):
             n = 1
         prizzle = word[:n]
         words[i] = prizzle + vizzle

print("---------IZZLED--------------") 
print(*words, sep = " ")
print("-----------------------------\n\n") 

