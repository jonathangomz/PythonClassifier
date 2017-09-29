#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:50:30 2017

@author: Jonathan
"""
# Labels:
# Redness	Yellowness	Mass	   Volumen 	Class
#
#
#######################################
############### IMPORTS ###############
#######################################

import sys
sys.path.insert(0, '/Users/Jonathan/Desktop/Jonathan/Programacion/Python/PythonForClass/machinelearning/Ch02/Classifier')
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as kNN
from sklearn import preprocessing

#######################################
############## FUNCTIONS ##############
#######################################

#Pass the data from file to matrix
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
        
#Train the program
def trainWithData(dataValue, dataLabel, n=10):
    valueNorm = preprocessing.normalize(dataValue, norm='l2')
    neighbor = kNN(n_neighbors=n)
    neighbor.fit(valueNorm, dataLabel)
    return neighbor

#Well... this don't need explain
def classify(neighbor, v2c):
    ans = neighbor.predict([v2c])
    return ans

#Introduce the values to classify
def inputValuesToClassify(mtx=None):
    valuesToClassify = []
    i = 0
    if mtx is None:
        while True:
            try:
                valuesToClassify.append(onlyNum(i))
                i += 1
                ans = (raw_input("¿Terminaste de ingresar los valores? [y]\n"))
                if ans == 'Y' or ans == 'y':
                    break
            except Exception, e:
                print "Ingresa un valor válido con números. Error [3]"
    else:
        for typeValue in range(len(mtx[0])):
            mtx[1][typeValue] = onlyNum(mtx[0][typeValue])
            valuesToClassify.append(mtx[1][typeValue])
    return valuesToClassify

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
            
#Learn with input values
""""""" Not ready YET """""""
def learn(v2l, l2l, values, labels):
    labels += [l2l[0]]
    values.append(v2l)#AttributeError: 'numpy.ndarray' object has no attribute 'append'
    return values, labels
        
#Run all functions
def runProgram(filename="testFruit.csv"):
    values, labels  = file2matrix(filename)
    mtxTypes        = inputTH(filename)
    n               = trainWithData(values, labels)
    v2c             = inputValuesToClassify(mtxTypes)
    r               = classify(n, v2c)
    return r
    
######################## In waitlist ########################
#                                                           #
#    def rejectOutliersFromList(data, m = 2.):              #
#        d = np.abs(data - np.median(data))                 #
#        mdev = np.median(d)                                #
#        s = d/mdev if mdev else 0                          #
#        return data[s<m]                                   #
#                                                           #
#    def rejectOutliersFromMatrix(dataSet):                 #
#        i = 0                                              #
#        for column in dataSet[:,i]:                        #
#            dataSet[:,i] = rejectOutliersFromList(column)  #
#                                                           #
#############################################################


#######################################
############### ADDS ON ###############
#######################################

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
    
#Return num of columns and lines
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
   
    
    
