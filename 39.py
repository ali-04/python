
def email_b (x):
    y = x.split('@')
    if len(y)==2 and len(y[1].split('.')) == 2 :
        return True
    else:
        return False





import mysql.connector

h = input('host: ')
u = input('user: ')
p = input('password: ')
d = input('database: ')
t = input('table: ')

sql = mysql.connector.connect ( user=u , host=h , password=p , database=d )

db = sql.cursor()

a = 'aa'

while not(email_b(a)):

    a = input('email: ')
    b = input('pass : ')
    if not(email_b(a)) :

        print ('email not correct!!')


db.execute('INSERT INTO %s (username  ,password) VALUES ("%s" ,"%s")' %(t,a,b))



sql.commit()





#mydb = db.fetchall()

#mydb.sort(  key=lambda x : x[2]   )


#for q in range(0,len(mydb)-1) :
#    if mydb[q][2] == mydb[q+1][2]:
#        if mydb[q][1] < mydb[q+1][1]:
#            x = mydb[q]
#            mydb[q] = mydb[q+1]
#            mydb[q+1] = x


#print (mydb)


#for y in range(len(mydb)-1,-1,-1):
#    q = mydb[y]
#    print (q[0],q[1],q[2])









