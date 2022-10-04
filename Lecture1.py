#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:20:00 2022

@author: inf-30-2022
"""
print ("Hello World")

"""
#This is a comment, will not be executed in code
"Use this for longer comments"

"""
print("How do I feel today?")
for i in range(0,10):
    if i>5:
        print(i, "#-I am happy")
    else:
        print(i,"#-Not so great")
print("End of Script")
#%%
print(type(1))
print(type("GATCCT"))
print(type("TRUE"))
print(type(True))
"print(type(true))" #Error, you need to type True
print(type(0))
print(type(0.00))
#%%
x=5
y=90
print(x,y)
print(x+y)
x='5'
y='Hus'
print(x,y)
print(x+y)
#%%
mass=5
volume=1.08
density=mass/volume
print(density)
#%%
"print(log10(100))" #cant define log10, need to import math program
import math
print(math.log10(100))
#%%
"Exercise Solve with Python"
"1. Second power of five"
print(5**2) #** är upphöjt till

"2. Square root of 16"
print(16**0.5)
print(math.sqrt(16))

"3.The remainder of 7 divided by 3"
print(7%3)

"4.The absolute value of -0.777"
print(abs(-0.777))

"5.Round 5.4 and 5.5"
print(round(5.4))
print(round(5.5))

"6.Round 6.7777888 to the third decimal point"
print(round(6.7777888, 3))

"7.Convert 7.7 to integer plus 8 to it"
print(round(7.7)+8)

"8.What is the minimum of 5,2,7 and maximum of 3,5,0.9?"
print(min(5,2,7))
print(max(3,5,0.9))

"9.What is log10 of 100?"
print(math.log10(100))

"10.What is the sixth digit of pi?"
print(str(math.pi)[6])
#%%
import random
print(random.random())
print(random.randrange(1,10))
print(random.choice('abcd'))
number_list=[7,14,21,28,35,42,49,56,63,70]
print("Original list:",number_list)
#%%
Seq='ABCDEFGHIJKLMNOP'
print(Seq[0])
print(Seq[0:3])
print(Seq[-3:-1])
print(Seq[0:5:2])
#%%
myDNA="ACGTAGCTAGCTAGTGT"
yourDNA="AAACCCGGGTTT"
"1.Count the number of G's in myDNA"
print(myDNA.count("G"))
