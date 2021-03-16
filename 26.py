from os import getcwd 
from csv import reader 

dd = '\\'
location = dd [0].join((getcwd() + dd[0] +"1.csv").split()) 
#print (location)

with open (location) as f :
    print (type (f))
    data = list(reader(f))
    print (data)























