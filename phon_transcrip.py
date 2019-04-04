#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import collections
import sys
import funciones as fn
import codecs


# las siguientes tres líneas abren el archivo 'input' y lo guardan en un string y de una lo pasa a minúsculas todo
inputa=str(sys.argv[1])
file = open(inputa)
text1 = file.read()
file.close()

#Pasa a minuscula y quita cambios de linea (\n) y los tab (\r) para que no cuente n's de más
text_min=text1.lower().replace("\n"," ").replace("\r"," ")

tildes= int(input('ingrese 0 para analisis sin tildes, ingrese 1 para analisis con tildes'))

if tildes==0:
	text = fn.quitatildes(text_min)
else:
	text = text_min

text_ph=fn.phonemize(text)

hile = codecs.open('output_marked.txt', 'w','utf-8-sig')
print(text_ph, file = hile)
hile.close()

text_final = fn.no_punct(text_ph)

iile = codecs.open('output_nopuncmarks.txt', 'w', 'utf-8-sig')
print(text_final, file = iile)
iile.close()
