# -*- coding: utf-8 -*-

"""
Created on Fri Oct 6 14:09:01 2017

@author: Jonathan
"""
#   WARNING: Functions with (*) aren't ready
# NOTE: Still rest fix the type in the funtion seeAll() in class Document


#######################################################################
############################### IMPORTS ###############################
#######################################################################

import os
import numpy as np
import codecs

#######################################################################
########################### MAIN FUNCTIONS ############################
#######################################################################
####### GLOBAL VARIABLES #######
tableHeadersAreOk = False

#Pass the data from file to a matrix using other three functions.
def file2matrix(filename, quitHeaders=False, changeWords=True):
    v, l, allData = file2matrixStr(filename, quitHeaders)
    if v != 0 and l != 0:
        if changeWords:
            v,dic = wrd2num(v)
            v = str2float(v)    #I dont remember why i do this function. The values put in float from the start.
        allData = str2float(allData)
        return v, l, dic, allData
    else:
        print("Error: 0 columnas [1.1]")
        return 0,0,0,0

#######################################################################
#Make, with the file, a matrix with the values of type str.
def file2matrixStr(filename, quitHeaders=False):
    chk, frm = checkFormat(filename)
    if chk:
        numLines, numColumn = sizes(filename)
        if numColumn != 0:
            allData = []
            classData = []  
            classLabel = []               
            fr = codecs.open(os.path.join("Documents",filename), 'r', 'utf-8')
            if quitHeaders:
                fr.readline()
            index = 0
            for line in fr.readlines():
                line = line.strip()
                listFromLine = line.split(frm)
                allData.append(listFromLine)
                classData.append(listFromLine[0:numColumn])
                classLabel.append(listFromLine[-1])
                index += 1
            return classData,classLabel, allData
        else:
            print("Error: 0 columnas [1]")
            return 0, 0, 0
    else:
        print "No pasó el chequeo del formato [2]"
        return 0, 0, 0

#Change the words in the file to numbers 
def wrd2num(values):
    valuesCleanUnorder  = []         #value Clean unorder
    valuesCleanOrder    = []
    dic                 = []
    for i in range(len(values[0])):
        arr                 = [t[i] for t in values]
        dicVal              = {}
        arrContainerTemp    = []
        count               = 0
        for t in arr:
            try:
                t = float(t)
            except:
                pass
            if t not in dicVal and not isinstance(t, float):
                if t == '':             #if contains an empty space change it with cero
                    arrContainerTemp.append(0)
                else:
                    arrContainerTemp.append(count+1)
                    dicVal[t] = count+1
                    count += 1
            elif isinstance(t, float):  #if is a number dont change it
                arrContainerTemp.append(t)
            else:                       #if already are in the array just put the value asigned to that variable
                arrContainerTemp.append(dicVal[t])
        dic.append(dicVal)
        valuesCleanUnorder.append(arrContainerTemp)
    tupO = zip(*valuesCleanUnorder[::-1])
    arrT = []
    for i in tupO:
        arrT = [t for t in reversed(i)]
        valuesCleanOrder.append(arrT)
    return valuesCleanOrder, dic

#change the type of the values to float
def str2float(data):
    y = 0
    v = [i[:] for i in data]
    for i in v:
        x = 0
        for t in i:
            try:
                v[y][x] = float(t)
            except:
                v[y][x] = t
            x += 1
        y += 1
    return v


##########################################################################################
    
#Returns the number of columns and rows
def sizes(filename, countColumn = True, countRows=True, check=False):
    isOk = True
    if check:
        isOk,_ = checkFormat(filename)
    if isOk:
        fr        = open(os.path.join("Documents",filename))
        numColumn = 0
        numLines  = 0
        if countColumn:
            if ',' in fr.readline():
                numColumn = len(fr.readline().strip().split(','))-1
            elif '\t' in fr.readline():
                numColumn = len(fr.readline().strip().split('\t'))-1
            else:
                print("Error en el formato: Los datos deben de estar separados por Coma o Tab [3]")
        if countRows:
            fr        = open(os.path.join("Documents",filename))
            numLines  = len(fr.readlines())
        fr.close()
        return numLines, numColumn
    else:
        print "Error con el formato [4]"
        return 0,0
 
def saveHeaders(filename):
    isOkH, headerLine = checkHeader(filename)
    if isOkH:
        f = open('Headers.txt', 'w+')
        for tH in headerLine:
            f.write(' %s ' %tH)
        f.close()
        return True, headerLine
    else:
        print("Hubo un error con el chequeo [5]")
        return False, 0

#######################################################################
################################ INPUT ################################
#######################################################################
    
#Ask if the table have headers. 
#>>Anyway we will check the headers, the user can be an asshole.<< 
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
def inputTH(filename=None, mtx=[]):
    lst = []
    if not mtx:         # si no se introduce matriz con th ejecutará cualquiera de las otras dos opciones
        if filename is not None:    #si se introuce un documento puede saber cuantos values se introducirán por su no. de columnas
            isOk,_ = checkFormat(filename)
            if isOk:        #checa que este bien el formato del archivo
                _,numTH = sizes(filename)
                i = 0
                while i < numTH:
                    i += 1
                    lst.append(raw_input("¿De que tipo será tu %i valor?\n"%i))
                mtx += [lst]    #agrega la lista de nombres(*)
                mtx += [[0 for x in range(len(mtx[0])-1)]]    #agrega una lista vacía donde irán los valores de cada feature(**)
                return mtx
            else:
                print "Error con el formato [6]"
                return 0
        else:               #si no se introduce archivo preguntará infinitamente hasta que el usuario termine de ingresar las features
            i = 0
            while True:
                txt = raw_input("¿De que tipo será tu %i valor?\n" % (i+1))
                lst.append(txt)
                i += 1
                ans = (raw_input("¿Terminaste de ingresar los tipos? [y]\n"))
                if ans == 'Y' or ans == 'y':
                    mtx += [lst]            #lo mismo que en (*)
                    mtx += [[0 for x in range(len(mtx[0])-1)]]    #lo mismo que en (**)
                    return mtx
                    break
    else:   #si se introduce la lista de nombres no es necesario que el usuario los introduzca
        mtx += [[0 for x in range(len(mtx[0])-1)]]    #lo mismo que en (**)
        return mtx
      
#######################################################################
################################ CHECK ################################
#######################################################################    

#Check the table header(*CHECK*)
def checkHeader(filename, check=False):
    isOk = True
    if check:
        isOk,sptr = checkFormat(filename)   #return if its ok and type of separator (sptr)
    else:
        _,sptr = checkFormat(filename)      #only return the type of separator (sptr)
    if isOk:
        fr           = open(os.path.join("Documents",filename))
        headerLine   = fr.readline().strip().split(sptr)
        for i in headerLine:
            try:
                float(i)
                print "Hey there! You have a number like header,\nand thats supicious. [7]"
                fr.close()
                return False, [headerLine]
            except:
                pass
        fr.close()
        return True, [headerLine]
    else:
        print("Ocurrió un error con el formato [8]")
        fr.close()

#Verify if are separated by Coma or Tab and return the type of separator
def checkFormat(filename):
    try:
        fr = open(os.path.join("Documents",filename))
        if ',' not in fr.readline() and '\t' not in fr.readline():
            fr.close()
            print("Error en el formato: Los datos deben de estar separados por Coma o Tab [9]")
            return False, 0
        else:
            if ',' in fr.readline():
                fr.close()
                return True, ','
            if '\t' in fr.readline():
                fr.close()
                return True, '\t'
    except Exception, e:
        print('Ocurrio un error al leer el archivo. [10] ',e)
        return False, 0
    
#Verify that the input value is a number
def onlyNum(feature=None):      					
    while True:
        if feature is None:
            try:
                texto = raw_input("Ingresa el valor\n")
            except KeyboardInterrupt, e:
                print("Se interrumpió el proceso")
        else:
            try:
                texto = raw_input("Ingresa el valor de "+ str(feature) + "\n")            
            except KeyboardInterrupt, e:
                print("Se interrumpió el proceso")
        try:
            num = float(texto)
            break
        except ValueError:
            print "Solo se aceptan numeros: "
    return num

#################################################################################################
################################################################################################# 
##################################                             ##################################
##################################       Clase Documento       ##################################
##################################                             ##################################
#################################################################################################
#################################################################################################
"""

    La clase Documento representa al documento que se usará para entrenar
    el clasificador.
    
    Utiliza los métodos en este archivo para crear sus atributos iguales
    a los del archivo pero formateados listos para clasificar.

"""
class Documento:
    """Documento formateado para clasificar"""
    def __init__(self, nameFile=None, changeWords=True):
        if nameFile is None:
            self.width          = 0 #columns
            self.height         = 0 #lines
            self.features       = []
            self.values         = []
            self.allData        = []
            self.dic            = {}
            self.labels         = []
            self.filename       = 'None'
        else:
            isOk,_          = checkFormat(nameFile)
            self.filename   = nameFile
            if isOk:
                self.filename               = nameFile
                self.height, self.width     = sizes(self.filename)
                global tableHeadersAreOk
                if askHeader():
                    tableHeadersAreOk, headers = checkHeader(self.filename)
                    if tableHeadersAreOk:
                        self.features = inputTH(_,headers)
                    else:
                        self.features = inputTH(self.filename)
                else:
                    self.features = inputTH()
                try:
                    self.values, self.labels, self.dic, self.allData = file2matrix(self.filename, tableHeadersAreOk, changeWords)
                    tableHeadersAreOk = False
                except Exception, e:
                    print("Error al obtener valores y etiquetas. [Documento]", e[0])
            #else:
                #self.width          = 0
                #self.height         = 0
                #self.tableHeaders   = []
                #self.values         = []
                #self.dic            = {}
                #self.labels         = []
    def seeAll(self):
        for i in self.__dict__:
            print(str(i)+"\t\t "+str(self.__dict__[i])+"\t "+str(type(i)))
