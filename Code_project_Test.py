# -*- coding: utf-8 -*-
#author: Jonathan Gomez
#date: 10/10/2017
#	util:
'''
	num_filas = 87,510
'''
###
'''
		Imports.
'''
###
'''
import re
import os

from Format import Documento
'''
import codecs
import Format as Fr
from datetime import datetime
import usefull_functions as uf
###
'''
		1.- Extraer datos asistencias.
'''
###
'''
regex_matricula = '[0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
regex_date 		= '[0-9][0-9][\/][0-9][0-9][\/][0-9][0-9]'
regex_type		= '[\'][0-1][0-1][0-1][\']'

fr = open(os.path.join("Documents",'export.txt'))
line = fr.readline()

documentFormated = []

for line in fr.readlines():
	matricula = re.search(regex_matricula, line)
	date = re.search(regex_date, line)
	tipo = re.search(regex_type, line)
	documentFormated.append([int(matricula.group(0)), date.group(0), float(tipo.group(0).strip("'"))])

f = open('newFile.txt', 'w+')
for data in documentFormated:
	for value in data:
		f.write('%s,' %value)
	f.write('\n')
f.close()
'''
###
'''
		2.- Testing the result file
'''
###
'''
fr = open('comedor-asistencias.txt')
fr.readline()
print(fr.readline().split(","))
print(fr.readline().split(","))
print(fr.readline().split(","))
print(fr.readline().split(","))
'''
###
'''
		3.- Juntar datos.
'''
###
'''
ciclo_academico 	= Documento('comedor-ciclo_academico.csv')

asistencias 		= Documento('comedor-asistencias.txt')
carreras 			= Documento('comedor-carreras.csv')
sexo_y_nacimiento 	= Documento('comedor-sexo-nacimiento.csv')
tipo_comidas 		= Documento('comedor-tipo_comidas.csv')

array 				= []
dicCarreras 		= {}
dicSexNac 			= {}

count 				= 0

print(asistencias.allData[0])

for i in carreras.allData:
	dicCarreras[i[0]] = i[1]
for i in sexo_y_nacimiento.allData:
	dicSexNac[i[0]] = [i[1], i[2]]

for a in asistencias.allData:
	matricula = a[0]
	try:
		a.append(dicCarreras[matricula])
		a.append(dicSexNac[matricula][0])
		a.append(dicSexNac[matricula][1])
		array.append(a)
	except Exception, e:
		print(e)
		pass
	print(a)
	count += 1
	print("Restan: %d" %(asistencias.height - count))

asistencias.allData[0]
asistencias.allData[1]
asistencias.allData[2]

f = codecs.open('newFile.txt', 'w+', 'utf-8')
for data in array:
	for value in data:
		f.write('%s,' %value)
	f.write('\n')
f.close()
'''
#
'''
		4.- Separar fecha.
'''
#
today = datetime.today()
date_format = '%d/%m/%y'

fr = codecs.open('newFile.txt', 'r', 'utf-8')
print(fr.readline().strip().split(','))
for line in fr.readlines():
 	line = line.strip()
 	listFromLine = line.split(',')
 	date = listFromLine[1].split('/') 	
 	if int(date[2])==17:
 		date_birth = listFromLine[5].split('/')
 		if date_birth[2] <= '17':
 			birth = datetime((2000+int(date_birth[2])), int(date_birth[0]), int(date_birth[1]), 0, 0, 0)
 		else:
 			birth = datetime((1900+int(date_birth[2])), int(date_birth[0]), int(date_birth[1]), 0, 0, 0)
 		diff  = today - birth
 		years = str(diff/365).split(' ')[0]
 		if int(years) not in list_edades:
 			list_edades.append(int(years))
 		order.append([listFromLine[4], int(years), listFromLine[3].strip(), listFromLine[2], int(date[0]), int(date[1]), uf.datetoday(int(date[0]), int(date[1]), 2000+int(date[2]))])

# Intercambiar palabras por números y obtener diccionario
order, dic = Fr.wrd2num(order)
print(list_edades)
'''
f = codecs.open('newFile2.csv', 'w+', 'utf-8')

for data in order:
	count = 0
	for value in data:
		if count != 6:
			f.write('%s, ' %value)
		else:
			f.write('%s' %value)
		count += 1
	f.write('\n')
f.close()
#sexo, edad, carrera, tipo_comida, dia_mes, mes, dia_semana
for i in dic:
	print(i)
'''
#
'''
	Next steps:
	 	-> separate the date.
	 	-> make a function which detect the day of any date.
		-> think which column will be the labels.
		-> think, think, think... think a lot. 
		-> Fuck.
'''
#





