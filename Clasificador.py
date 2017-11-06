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
import Format as Frm
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.dummy import DummyClassifier

#clf = DummyClassifier(strategy='most_frequent',random_state=0)
#clf.fit(X_train, y_train)
#clf.score(X_test, y_test)  

####################################################################################################
####################################################################################################
################################                                    ################################
################################           MAIN FUNCTIONS           ################################
################################                                    ################################
####################################################################################################
####################################################################################################
#####################
#####################
""" Gloabal Variables """
ans        = 0.0    #Used in classify() and inputValuesToClassify()
score      = 0.0    #Used in accuracy()
ValuesTest = []     #Used in accuracy()
labelsTest = []     #Used in accuracy()
#####################
#####################
###################### Classifiers ###################### 
def knnClas(values, labels, n=10):
    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(values, labels)
    return knn

def logregClas(values, labels, c=1e5):
    LogReg = LogisticRegression(C=c)
    LogReg.fit(values, labels)
    return LogReg

def svmClas(values, labels):
    svm = SVC()
    svm.fit(values, labels)
    return svm

def treeClas(values, labels):
    tree = DecisionTreeClassifier()
    tree.fit(values, labels)
    return tree

def dummyClas(values, labels):
    dummy = DummyClassifier(strategy='most_frequent',random_state=0)
    dummy.fit(values, labels)
    return dummy

###################### Classify ######################
def classify(classifier, v2c):
    ans = classifier.predict([v2c])
    return ans

###################### Accuracy ######################
def accuracy(classifier, values, labels, porcentaje=0.66, testClassifier=False):
    num = int(len(values)*porcentaje)
    valuesTest = values[0:num]
    labelsTest = labels[0:num]
    score = classifier.score(valuesTest, labelsTest)
    if testClassifier:
        dummy = dummyClas(values, labels)
        ansDummy = dummy.score(valuesTest, labelsTest)
        return score, ansDummy
    else:
        return score

###################### Input Values ######################
#I think this dont need explain, the title is so explicit :P
def inputValuesToClassify(mtx=None, knowValuesFeatures=False):
    val2cls = []
    if mtx is None:
        i = 0
        while True:
            try:
                val2cls.append(Frm.onlyNum(i))
                i += 1
                ans = (raw_input("¿Terminaste de ingresar los valores? [y]\n"))
                if ans == 'Y' or ans == 'y':
                    break
            except Exception, e:
                print "Ingresa un valor válido con números. Error [3]"
    else:
        for positionValue in range(len(mtx[0])-1):
            mtx[1][positionValue] = Frm.onlyNum(mtx[0][positionValue])
            val2cls.append(mtx[1][positionValue])
    if knowValuesFeatures:
        return val2cls, mtx
    else:
        return val2cls

#################################################################################################
#################################################################################################     
##################################                             ##################################
##################################      Clase Classifiers      ##################################
##################################                             ##################################
#################################################################################################
#################################################################################################

class Classifiers:
    """ Implementa cuatro clasificadores diferentes.
        
    Genera un objeto que incluye atributos que ayudan a combinar
    cuatro diferentes clasificadores: kNN, Logistic Regression, SVM y 
    Desicion Tree.

    #Parámetros:
    dataValues -- matrix que incluye los valores con los que se entrenaran los clasificadores.
    dataLabels -- matrix que incluye las clases con los que se entrenaran los clasificadores.
    classifier -- Clasificadores que se utilizarán. Predeterminado todos.

    #Atributos:
    values          -- valores introducidos.
    labels          -- clases introducidas.
    val2cls         -- valores introducidos por el usuario.
    mtxClas         -- valores introducidos por el usuario con la feature a la que pertenecen.
    listClassifiers -- lista de clasificadores utilizados.
    listAns         -- lista de clasificacciones hechas por los clasificadores usados.
    listScore       -- lista de Scores resultantes de los clasificadores usados.
    score           -- Score de un clasificador específico.
    dummyAns        -- score del clasificador dummy.

    #Clasificadores:
    dummy           -- clasificador Dummy.
    knn             -- clasificador KNeighbor Nearest.
    logreg          -- clasificadore Loigstic Regresion.
    svm             -- clasificador Support Virtual Machine.
    tree            -- clasificador Desicion Tree.


    """
    def __init__(self, dataValues, dataLabels, classifier=""):
        self.values = preprocessing.normalize(dataValues, norm='l2')
        self.labels = dataLabels
        self.dummy = dummyClas(self.values, self.labels)
        self.listClassifiers = {}
        if classifier == "" or "KNN" in classifier:
            self.knn = knnClas(self.values, self.labels)
            self.listClassifiers['KNN'] = self.knn
        if classifier == "" or "LogReg" in classifier:
            self.logreg = logregClas(self.values, self.labels)
            self.listClassifiers['logreg'] = self.logreg
        if classifier == "" or "SVM" in classifier:
            self.svm = svmClas(self.values, self.labels)
            self.listClassifiers['svm'] = self.svm
        if classifier == "" or "Tree" in classifier:
            self.tree = treeClas(self.values, self.labels)
            self.listClassifiers['Tree'] = self.tree
        if self.listClassifiers == {}:
            print("Ingresa un clasificador correcto [KNN, LogReg, SVM, Tree]")

    def inputValuesToClassify(self, mtx=None, knowValuesFeatures=False):
        """Ingresa los valores para clasificar.

        Devuelve la lista de valores a evaluar. También puede regresar
        una lista con cada característica a la que se agregó cada valor.

        Parámetros:
        mtx -- matríz con las características. Predeterminado ninguna.
        knowValuesFeatures -- si se desea conocer el valor de cada característica. Predeterminado False.

        """
        if knowValuesFeatures:
            self.val2cls, self.mtxClas = inputValuesToClassify(mtx, knowValuesFeatures)
        else:
            self.val2cls = inputValuesToClassify(mtx)

    def classify(self, classifier=None):
        """Predice la clase usando algún clasificador.
        
        Devuelve la clase resultante. También puede regresar un diccionario 
        con los resultados de cada clasificador usado.

        Parámetros:
        classifier -- clasificador que se usará. Predeterminado todos.

        """
        if classifier != None:
            global ans
            ans = classify(classifier, self.val2cls)
            return ans
        else:
            self.listAns = {}
            for clas in self.listClassifiers:
                self.listAns[clas] = self.classify(self.listClassifiers[clas])
            return self.listAns

    def accuracy(self, classifier=None, porcentaje=0.66, testClassifier=False):
        """Calcula el promedio de eficiencia del clasificador.
        
        Devuelve el promedio de eficiencia de algún clasificador. Puede regresar
        un diccionario con el promedio de eficiencia de cada clasificador usado.

        Parámetros:
        classifier -- clasificador que se usará. Predeterminado todos.
        porcentaje -- porcentaje de los valores que usará para las pruebas. Predeterminado 66%.
        testClassifier -- si se comparar con el clasificador Dummy. Predeterminado False.

        """
        if classifier != None:
            if testClassifier:
                self.score, self.dummyAns = accuracy(classifier, self.values, self.labels, testClassifier=True)
                return self.score, self.dummyAns
            else:
                self.score = accuracy(classifier)
                return self.score
        else:
            self.listScores = {}
            for idClassifier in self.listClassifiers:
                self.listScores[idClassifier] = accuracy(self.listClassifiers[idClassifier], self.values, self.labels, testClassifier=testClassifier)
            return self.listScores

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
    