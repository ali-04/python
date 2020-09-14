r = input ()
ja = "hello"
b = 0
lll = 0
for t in ja :

    if r.find(t,b) == -1 :
        print ('NO')
        lll = 1 
    else:
        print (t)
        print (b)
        b = r.find(t,b) + 1


if lll == 0:
    print ("YES")



























