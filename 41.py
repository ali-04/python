
from bs4 import BeautifulSoup

from requests import get

e = get('https://divar.ir/s/tehran')


soup = BeautifulSoup(e.text,'html.parser')
  
  
val = soup.findAll('a')

c = 0

for q in val[36:] :
    ee = q.text
    if 'توافقی' in ee:
        print ('\n\n\n\n%i:\n%s'%(c,ee))
        c+=1










    

