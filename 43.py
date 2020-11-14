
from bs4 import BeautifulSoup

from requests import get


def give_data (page)

    e = get("https://bama.ir/car/all-brands/all-models/all-trims?page=%i" %page)


    soup = BeautifulSoup(e.text,'html.parser')
  
  
    val = soup.findAll('li')

    c = 0

    








































