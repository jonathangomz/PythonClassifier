# -*- coding: utf-8 -*-
#
'''
        CAMBIAR UN NÚMERO CON LETRA A UNO DE TIPO NÚMERICO
'''
#
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

# EXAMPLE:
#print(text2int("one hundred twenty two"))
#

################################################################################

#
'''
        CALCULA EL DIA DE LA SEMANA DE UNA FECHA ESPECÍFICA
'''
#
days = [ 'Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado' ]

def datetoday(dia, mes, ano):
    d = dia
    m = mes
    y = ano
    if m < 3:
        z = y-1
    else:
        z = y
    dayofweek = ( 23*m//9 + d + 4 + y + z//4 - z//100 + z//400 )
    if m >= 3:
        dayofweek -= 2
    dayofweek = dayofweek%7
    if dayofweek == 7:
      dayofweek = 1
    else:
      dayofweek += 1
    return dayofweek

#EXAMPLE:
#print(days[datetoday(int(date[0]), int(date[1]), 2000+int(date[2]))])
#