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
#
#Note: ApacheSpark
# ******   Split data for testing   ******
#######################################################################
############################### IMPORTS ###############################
#######################################################################

import sys
sys.path.insert(0, '/Users/Jonathan/Desktop/Jonathan/Programacion/Python/PythonForClass/machinelearning/Ch02/Classifier')
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as kNN 
from sklearn import preprocessing, tree, svm, linear_model
import Format as Frm
from sklearn.dummy import DummyClassifier

#>>> clf = DummyClassifier(strategy='most_frequent',random_state=0)
#>>> clf.fit(X_train, y_train)
#DummyClassifier(constant=None, random_state=0, strategy='most_frequent')
#>>> clf.score(X_test, y_test)  

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

#Introduce the values to classify
def inputValuesToClassify(mtx=None, knowValuesFeatures=False):
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
        for positionValue in range(len(mtx[0])-1):
            mtx[1][positionValue] = Frm.onlyNum(mtx[0][positionValue])
            valuesToClassify.append(mtx[1][positionValue])
    if knowValuesFeatures:
        return valuesToClassify, mtx
    else:
        return valuesToClassify

#Well... this don't need explain
def classifyKnn(dataValue, dataLabel, v2c, n=10):
    knnClas = kNN(n_neighbors=n)
    valueNorm = preprocessing.normalize(dataValue, norm='l2')
    knnClas.fit(valueNorm, dataLabel)
    ans = knnClas.predict([v2c])
    return ans                

def classifyTree(dataValue, dataLabel, v2c):
    treeClas = tree.DecisionTreeClassifier()
    dataValue = preprocessing.normalize(dataValue, norm='l2')
    treeClas.fit(dataValue, dataLabel)
    ans = treeClas.predict([v2c])
    return ans

def classifySVM(dataValue, dataLabel, v2c):
    svmClas = svm.SVC(kernel='rbf', C=1)
    dataValue = preprocessing.normalize(dataValue, norm='l2')
    svmClas.fit(dataValue, dataLabel)
    ans = svmClas.predict([v2c])
    return ans

def classifyLogReg(dataValue, dataLabel, v2c):
    logisticClas = linear_model.LogisticRegression(C=1e5)
    dataValue = preprocessing.normalize(dataValue, norm='l2')
    logisticClas.fit(dataValue, dataLabel)
    ans = logisticClas.predict([v2c])
    return ans

#Testing classifiers
def testClassifiers(mtxValues, mtxLabels, checkClassifier="", porcentaje=0.66):
    numPorcentaje = int(len(mtxValues)*porcentaje)
    mtxValuesTest = mtxValues[0:numPorcentaje]
    mtxLabelsTest = mtxLabels[0:numPorcentaje]
    mtxAnsTest = []
    ansClassifier = 0.0
    #Evalua los clasificadores
    for x in xrange(len(mtxValuesTest)):
        val = mtxValuesTest[x]
        if checkClassifier is "KNN":
            ansClassifier = classifyKnn(mtxValuesTest, mtxLabelsTest, val)
        elif checkClassifier == "LogReg":
            ansClassifier = classifyLogReg(mtxValuesTest, mtxLabelsTest, val)
        elif checkClassifier == "SVM":
            ansClassifier = classifySVM(mtxValuesTest, mtxLabelsTest, val)
        elif checkClassifier == "Tree":
            ansClassifier = classifyTree(mtxValuesTest, mtxLabelsTest, val)
        elif checkClassifier == "":
            ansClassifierKnn = classifyKnn(mtxValuesTest, mtxLabelsTest, val)
            ansClassifierLogReg = classifyLogReg(mtxValuesTest, mtxLabelsTest, val)
            ansClassifierSVM = classifySVM(mtxValuesTest, mtxLabelsTest, val)
        else:
            ansClassifier = 0.0
            print("Nombre de clasificador incorrecto. Opciones: KNN, LogReg y SVM.")
            break
        if checkClassifier == "":
            ansClassifier = -1
            mtxAnsTest.append([ansClassifierKnn, ansClassifierLogReg, ansClassifierSVM])
        else:
            if ansClassifier != 0.0:
                mtxAnsTest.append(ansClassifier)
            else:
                print("Error")
    countError = 0.0
    testMtx = []
    if ansClassifier == 0.0:
        return testMtx, 0.0
    else:
        #junta la matriz de las respuestas con la del los labels del dataset
        for x in xrange(len(mtxAnsTest)):
            if(mtxAnsTest[x][0] != mtxLabels[x]):
                countError += 1
            if checkClassifier == "":
                for y in xrange(len(mtxAnsTest[0])):
                    testMtx.append([mtxAnsTest[x][y][0], mtxAnsTest[x][y][0], mtxAnsTest[x][y][0], mtxLabels[x]])
            else:
                testMtx.append([mtxAnsTest[x][0], mtxLabels[x]])
        return testMtx, float(countError/float(numPorcentaje))

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
    