# -*- coding: utf-8 -*-
from __future__ import print_function
from collections import Counter
import sys
import unicodedata
import string
import re
import pandas as pd
import matplotlib.pylab as plt



def phonemize(text1):
	inputa='phonemiz_esp_tild.txt'#input("ingrese el nombre del archivo con el mapeo fonético que desea implementar: ")
	file = open(inputa)
	grapheme_list = []
	phoneme_list = []

	for line in file:
		line = line.split('*')
		if not line:  # empty line?
			continue
		grapheme_list.append(str(line[0]))
		phoneme_list.append(str(line[1].replace('\n','')))
	print(grapheme_list)
	print( '\n')
	print( phoneme_list)


	for i in range(len(grapheme_list)):
		text1=text1.replace(str(grapheme_list[i]),str(phoneme_list[i]))


	return text1   

def no_punct(text):
	#Quita puntuacion del texto
	sign_list = [u'¡',u'"',u'¿',u'—',u'“',u'-',u'”',u'º',u'¿',u'—',u'“',u'-',u'”',u'¡',u'1',u'2',u'5',u'6',u'7',u'8',u'0',u'º',u'9',u'4',u'3',u'«',u'»',u'.',u'–',u'’',u'...',u'\n', u'\r']
	for sign in sign_list:
		text=text.replace(sign,'')

	return re.sub('[%s]' % re.escape(string.punctuation), '', text)
	
	#otra opcion:

# tbl = dict.fromkeys(i for i in range(sys.maxunicode)
#					   if unicodedata.category(chr(i)).startswith('P'))
# def remove_punctuation(text):
#	 return text.translate(tbl)

def counter(text1):
	"""mide las frecuencias relativas de cada caracter"""
	
	c_counter = collections.Counter(text1)
	graphema_list = list(c_counter)

	"obtenemos el total de caracteres contados:"
	graphema_sum=sum(c_counter.values())
	abc_str = "".join(x for x in graphema_list)

	"de forma que abc_string es el abecedario del texto procesado"
	count_dict=dict(c_counter)


	return count_dict

def distribucion_acento(text_ph):#Recibe texto phonemizado
	contador_palabras = Counter()
	for line in text_ph.splitlines():
		contador_palabras.update(line.split())
	palabras_dict = dict(contador_palabras)

	#Cargar palabras por no contar (no acentuadas):
	inputa = 'no_acent.txt'
	file = open(inputa)
	no_acent_text = file.read()
	file.close()
	#fonemizacion de las palabras no acentuadas
	no_acent_text_ph = phonemize(no_acent_text).replace('[','').replace(']','')
	lista_no_acent = no_acent_text_ph.split('*')
	#Lo siguiente suma sólo las palabras no acentuadas
	suma=0
	for key in palabras_dict:
		if key not in lista_no_acent:
			suma = suma + palabras_dict[key]


	Contador = Counter(text)
	Contador['#'] = suma

	Data = pd.DataFrame.from_dict(Contador, orient='index', columns = ['Frecuencia'])
	Data['Fraccional'] = Data['Frecuencia']/sum(Data['Frecuencia'])
	Data = Data.sort_values(by = 'Fraccional', ascending = False)
	fig = plt.figure(figsize = (10,8))
	plt.plot(Data['Fraccional'], 'mo')
	plt.show()
	return fig, Data


def quitatildes(text1):
	
	return ''.join(c for c in unicodedata.normalize('NFD', text1)
				  if unicodedata.category(c) != 'Mn')
