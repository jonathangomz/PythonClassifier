#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:50:30 2017

@author: Jonathan
"""
# Labels:
# Redness	
# Yellowness	
# Mass	   
# Volumen 	
# Class
#######################################################################
############################### IMPORTS ###############################
#######################################################################

import sys
sys.path.insert(0, '/Users/Jonathan/Desktop/Jonathan/Programacion/Python/PythonForClass/machinelearning/Ch02/Classifier')
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as kNN 
from sklearn import preprocessing, tree
import Format as Frm

####################################################################################################
####################################################################################################
################################                                    ################################
################################           MAIN FUNCTIONS           ################################
################################                                    ################################
####################################################################################################
####################################################################################################

"""
            KNeighborsClassifier
"""  

#Train the program
def trainWithData(dataValue, dataLabel, n=10):
    valueNorm = preprocessing.normalize(dataValue, norm='l2')
    neighbor = kNN(n_neighbors=n)
    neighbor.fit(valueNorm, dataLabel)
    return neighbor

#Introduce the values to classify
def inputValuesToClassify(mtx=None):
    valuesToClassify = []
    i = 0
    if mtx is None:
        while True:
            try:
                valuesToClassify.append(Frm.onlyNum(i))
                i += 1
                ans = (raw_input("¿Terminaste de ingresar los valores? [y]\n"))
                if ans == 'Y' or ans == 'y':
                    break
            except Exception, e:
                print "Ingresa un valor válido con números. Error [3]"
    else:
        for typeValue in range(len(mtx[0])-1):
            mtx[1][typeValue] = Frm.onlyNum(mtx[0][typeValue])
            valuesToClassify.append(mtx[1][typeValue])
    return valuesToClassify

#Well... this don't need explain
def classifyKNN(neighbor, v2c):
    ans = neighbor.predict([v2c])
    return ans                

"""
            logRegres, Tree, Bayes
"""

def treeClas(dataValue, dataLabel, v2c):
    treecls = tree.DecisionTreeClassifier()
    treecls = treecls.fit(dataValue, dataLabel)
    ans = treecls.predict([v2c])
    return ans

#####################################################################
############################### Extras ##############################
#####################################################################

#Learn with input values
"""
             Not ready YET 
    Add more classifiers to do better
"""
def learn(v2l, l2l, values, labels):
    labels += [l2l[0]]
    values = np.vstack((values, v2l))

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
    