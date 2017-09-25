'''

Clasificador pa' la mushasha que quiere buscar un novio sin perder tiempo :v

Autor: Jonathan Gomez Perez
Date: 2017/09/24

'''

'''
#########################
******** IMPORTS ********
#########################
'''

from sklearn.neighbors import KNeighborsClassifier as kNN
import kNN as knn

'''
#########################
********FUNCTIONS********
#########################
'''

########
def act1(neighbors=3):					#Train the program
  dataSetValue, dataSetLabel = knn.file2matrix("datingTestSet2.txt")
  n = kNN(n_neighbors=neighbors)
  n.fit(dataSetValue, dataSetLabel)
  return n

#########
def onlyNum():      					#Check that only contains numbers
  while True:
    texto = raw_input()
    try:
      num = float(texto)
      break
    except ValueError:
      print "Solo se aceptan numeros"
  return texto

'''
#########################
**********JOB************
#########################
'''

neighbor = act1()

print "Ingresa el numero de millas viajadas por year: "
travel = onlyNum()
print "Ingresa el porcentaje de tiempo gastado jugando videojuegos: "
videogames = onlyNum()
print "Ingresa el numero de litros de nieve consumidos por semana: "
icecream = onlyNum()

dataSetValue, dataSetLabel = knn.file2matrix("datingTestSet2.txt")
n = kNN(n_neighbors=10)
n.fit(dataSetValue, dataSetLabel)
var = neighbor.predict([[travel, videogames, icecream]])

if var == '3':
  print "He will like her %s" % var
elif var =='2':
  print "Maybe like her %s" % var
elif var == '1':
  print "Better don't waste your time %s" % var
else:
  print 'Error 202'
