def wert (n):
    if len ((str(n)) [(int((str(n)).find ('.'))+1):] ) > 4 :
        return round (n,4)
    else:
        ee = str (n)
        while not(len ((str(ee)) [(int((str(ee)).find ('.'))+1):] ) >= 4):
            ee += "0" 
           # print (".")
        return  ee



e = int(input ())
w = list()
from math import sqrt


for a in range (0,e):
    w.append('')
    w [a] =  int (input())


for a in range (0,e):
    print (wert((sqrt( w[a]))))









