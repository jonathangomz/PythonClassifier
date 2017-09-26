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
from sklearn import preprocessing
import kNN as knn

'''
#########################
********FUNCTIONS********
#########################
'''

########
def act1(archivo="datingTestSet2.txt", neighbors=10):					#Train the program
  dataSetValue, dataSetLabel = knn.file2matrix(archivo)
   # print dataSetValue[0:20]
  valueNorm = preprocessing.normalize(dataSetValue, norm='l2')
   # print valueNorm[0:20]
  neighbor = kNN(n_neighbors=neighbors)
  neighbor.fit(valueNorm, dataSetLabel)
  return neighbor

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

########						#Check if the classifier works... i think so
def check():
  var1 = n.predict([[40920, 8.326976, 0.953952]])
  var2 = n.predict([[14488, 7.153469, 1.673904]])
  var3 = n.predict([[26052, 1.441871, 0.805124]])
  var4 = n.predict([[75136, 13.147394, 0.428964]])
  var5 = n.predict([[38344, 1.669788, 0.134296]])
  var6 = n.predict([[72993, 10.141740, 1.032955]])
  var7 = n.predict([[35948, 6.830792, 1.213192]])
  var8 = n.predict([[42666, 13.276369, 0.543880]])
  var9 = n.predict([[67497, 8.631577, 0.749278]])
  var10 = n.predict([[35483, 12.273169, 1.508053]])
  var11 = n.predict([[50242, 3.723498, 0.8319217]])
  var12 = n.predict([[63275, 8.385879, 1.669485]])
  var13 = n.predict([[5569, 4.875435, 0.728658]])
  print "var1: %s the right answer is 3" % var1
  print "var2: %s the right answer is 2" % var2
  print "var3: %s the right answer is 1" % var3
  print "var4: %s the right answer is 1" % var4
  print "var5: %s the right answer is 1" % var5
  print "var6: %s the right answer is 1" % var6
  print "var7: %s the right answer is 3" % var7
  print "var8: %s the right answer is 3" % var8
  print "var9: %s the right answer is 1" % var9
  print "var10: %s the right answer is 3" % var10
  print "var11: %s the right answer is 1" % var11
  print "var12: %s the right answer is 1" % var12
  print "var13: %s the right answer is 2" % var13

'''
#########################
**********JOB************
#########################
'''

n = act1()

print "Ingresa el numero de millas viajadas por year: "
travel = onlyNum()
print "Ingresa el porcentaje de tiempo gastado jugando videojuegos: "
videogames = onlyNum()
print "Ingresa el numero de litros de nieve consumidos por semana: "
icecream = onlyNum()

var = n.predict([[travel, videogames, icecream]])

if var == '3':
  print "She will like his %s" % var
elif var =='2':
  print "Maybe like her %s" % var
elif var == '1':
  print "Better don't waste your time %s" % var
else:
  print 'Error 202'

#check()
