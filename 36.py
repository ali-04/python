import datetime
u = input ()
ccc=[]
pq = u.split('/')
for xxx in pq :
    ccc.append(int(xxx))
pq = ccc
if len(str(pq [0]))!= 4 or len (pq) != 3 or len(str(pq [1]))!= 2  or pq [2] > 31 or pq [2] < 1 or pq [1] > 12 or pq [1] < 1 :
    print('WRONG')
else:
    q = ('-'.join(u.split('/')))

    x = datetime.date.fromisoformat(q)
    y = datetime.date.today()

    e = y-x

    print  (int(e.days)//365)










 

