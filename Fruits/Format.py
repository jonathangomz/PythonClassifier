# -*- coding: utf-8 -*-

"""
Created on Fri Oct 6 14:09:01 2017

@author: Jonathan
"""
#   WARNING: Functions with (*) aren't ready


#######################################################################
############################### IMPORTS ###############################
#######################################################################

import numpy as np

#######################################################################
########################### MAIN FUNCTIONS ############################
#######################################################################

#Pass the data from file to an matrix
def file2matrix(filename):
    chk, frm = checkFormat(filename)
    if chk:
        numLines, numColumn = sizes(filename)
        if numColumn != 0:
            classData = np.zeros((numLines,numColumn))     
            classLabel = []                        
            fr = open(filename)
            index = 0
            for line in fr.readlines():
                line = line.strip()
                listFromLine = line.split(frm)
                classData[index,:] = listFromLine[0:numColumn]
                classLabel.append(listFromLine[-1])
                index += 1
            return classData,classLabel
        else:
            print("Error: 0 columnas [1]")
            return 0, 0
    else:
        print "No pasó el chequeo del formato [2]"
        return 0, 0
    
#Returns the number of columns and rows
def sizes(filename, check=False):
    isOk = True
    if check:
        isOk,_ = checkFormat(filename)
    if isOk:
        fr        = open(filename)
        numColumn = 0
        if ',' in fr.readline():
            numColumn = len(fr.readline().strip().split(','))-1
        elif '\t' in fr.readline():
            numColumn = len(fr.readline().strip().split('\t'))-1
        else:
            print("Error en el formato: Los datos deben de estar separados por Coma o Tab [6]")
        fr        = open(filename)
        numLines  = len(fr.readlines())
        fr.close()
        return numLines, numColumn
    else:
        print "Error con el formato[7]"
        return 0,0
    
#######################################################################
################################ INPUT ################################
#######################################################################
    
def askHeader():
    ans = raw_input("¿Tu archivo tiene los titulos de las columnas?(y/n)\n")
    while True:
        if ans == 'y' or ans == 'Y':
            return True
            break
        elif ans == 'n' or ans == 'N':
            return False
            break
        else:
            print("No se reconoce la respuesta")
        ans = raw_input("¿Tu archivo tiene los titulos de las columnas?(y/n)\n")
        
#To know the TH (Table Headers)
def inputTH(filename=None):
    mtx = []
    lst = []
    if filename is not None:
        isOk,_ = checkFormat(filename)
        if isOk:
            _,numTH = sizes(filename)
            i = 0
            while i < numTH:
                i += 1
                lst.append(raw_input("¿De que tipo será tu %i valor?\n"%i))
            mtx += [lst]
            mtx += [[0 for x in range(len(mtx[0]))]]
            return mtx
        else:
            print "Error con el formato"
            return 0
    else:
        i = 0
        while True:
            txt = raw_input("¿De que tipo será tu %i valor?\n" % (i+1))
            lst.append(txt)
            i += 1
            ans = (raw_input("¿Terminaste de ingresar los tipos? [y]\n"))
            if ans == 'Y' or ans == 'y':
                mtx += [lst]
                txt += [[0 for x in range(len(mtx[0]))]]
                return mtx
                break
      
#######################################################################
################################ CHECK ################################
#######################################################################    

def checkHeaders(filename):
    print "Hello"
        
def checkHeader(filename):
    fr          = open(filename)
    headerLine   = fr.readline()
    return headerLine

#Verify if are separated by Coma or Tab and return the type of separator
def checkFormat(filename):
    try:
        fr = open(filename)
        if ',' not in fr.readline() and '\t' not in fr.readline():
            fr.close()
            print("Error en el formato: Los datos deben de estar separados por Coma o Tab [4]")
            return False
        else:
            if ',' in fr.readline():
                fr.close()
                return True, ','
            if '\t' in fr.readline():
                fr.close()
                return True, '\t'
    except Exception, e:
        print('Ocurrio un error al leer el archivo. [5] ',e)
        return False, 0
    
#Verify that the input value is a number
def onlyNum(count=None):      					
    while True:
        if count is None:
            texto = raw_input("Ingresa el valor\n")
        else:
            texto = raw_input("Ingresa el valor de "+ str(count) + "\n")            
        try:
            num = float(texto)
            break
        except ValueError:
            print "Solo se aceptan numeros"
    return num
    