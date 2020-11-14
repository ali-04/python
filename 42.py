
from requests import get
from bs4 import BeautifulSoup as soup
from re import findall as re
import mysql.connector


lis = list()

li = "https://www.truecar.com/used-cars-for-sale/listings/%s/%s/location-pittsburgh-pa/?searchRadius=5000&sortbest_match"  %(input('make: '),input('model: '))


s = get(li)

q = soup (s.text,'html.parser')

w = q.findAll('a')


e = 0
for x in w :
    a = re(r"price\$([\d,]+)\smiles([\d,]+)\smi",x.text)
    if a != []:
        lis.append(a[0])
    e+=1
        
    
if len(lis) > 30 :
    lis = lis[:30]



u = input('user: ')
p = input('pass: ')
h = input('host: ')
db = input('database: ')
table = input('table: ')



sql = mysql.connector.connect(
user=u 
,password=p
,host=h
,database=db  

)








mydb = sql.cursor()

for x,y in lis :

    mydb.execute('INSERT INTO %s (carcard  ,sel) VALUES ("%s" ,"%s")' %(table,x,y))


sql.commit()

