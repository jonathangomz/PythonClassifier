# -*- coding: utf-8 -*-
###
'''
		Imports.
'''
###
'''
import re
import os
from Format import Documento
import codecs
'''
###
'''
		Extraer datos asistencias.
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
		Testing the result file
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
		Juntar datos.
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
'''
#
	Next steps:
	 	-> separate the date.
	 	-> make a function which detect the day of any date.
		-> think which column will be the labels.
		-> think, think, think... think a lot. 
		-> Fuck.
#
'''




