#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:50:30 2017

@author: Jonathan
"""
# Labels:
# Redness	Yellowness	Mass	Volume	Class
#
#
#######################################
############### IMPORTS ###############
#######################################

import sys
sys.path.insert(0, '/Users/Jonathan/Desktop/Jonathan/Programacion/Python/PythonForClass/machinelearning/Ch02/Classifier')
import kNN as knn
from numpy import zeros
import operator
from os import listdir
from sklearn.neighbors import KNeighborsClassifier as kNN

#######################################
############## FUNCTIONS ##############
#######################################

#Pass the data from file to matrix
def file2matrix(filename):
    chk, frm = checkFormat(filename)
    if chk:#     Try to add a... gg, a Try and Exec
        numLines, numColumn = sizes(filename)
        if numColumn != 0:
            classData = zeros((numLines,numColumn))     
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
            print("Error")
            return 0, 0
    
#######################################
############### ADDS ON ###############
#######################################

#Check if are separated by Coma or Tab and return the type of separator
def checkFormat(filename):
    isOk = True
    try:
        fr = open(filename)
    except Exception, e:
        print("Ocurrio un error al leer el archivo. ",e)
        return False, 0
    
    if ',' not in fr.readline() and '\t' not in fr.readline():
        fr.close()
        print("Error en el formato: Los datos deben de estar separados por Coma o Tab [2]")
        return False
    else:
        if ',' in fr.readline():
            fr.close()
            return True, ','
        if '\t' in fr.readline():
            fr.close()
            return True, '\t'
    
#Return num of columns and lines
def sizes(filename):
    fr        = open(filename)
    numColumn = 0
    if ',' in fr.readline():
        numColumn = len(fr.readline().strip().split(','))-1
    elif '\t' in fr.readline():
        numColumn = len(fr.readline().strip().split('\t'))-1
    else:
        print("Error 202: Incorrect format")
    fr        = open(filename)
    numLines  = len(fr.readlines())
    fr.close()
    return numLines, numColumn
    
#Count the num of files
def countLines(filename):
    fr        = open(filename)
    print len(fr.readlines())    
    
    
