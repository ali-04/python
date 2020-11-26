import datetime
from re import findall as find

def WRONG ():
    print ('WRONG')
    exit()

u = input ()
def b_ad (ad):
    if find(r"(\d+)",ad)==[]:
        WRONG()
        return False
    elif find(r"(\d+)",ad)[0] != ad :
        WRONG()
        return False
    else :
        return True 


ccc=[]
pq = u.split('/')
for xxx in pq :
    if b_ad(xxx):
        ccc.append(int(xxx))

pq = ccc


if  find(r'(\d{4}/\d{1,2}/\d{1,2})',u) == None :
    WRONG()
elif find(r'(\d{4}/\d{1,2}/\d{1,2})',u) [0] != u:
    WRONG()



elif  pq [2] > 31 or pq [2] < 1 or pq [1] > 12 or pq [1] < 1 :
    WRONG()
else:
    q = ('-'.join(u.split('/')))

    x = datetime.date.fromisoformat(q)
    y = datetime.date.today()
    if x > y :
        WRONG()
    else:
    
        e = y-x

        frt = int (e.days) * 24 * 60 * 60


        print  (frt // 31557600)











 

