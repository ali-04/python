

jj = 0
f = input ()
f = int(f)
while f <= 0 :
    f = input ()
    f = int(f)

if f == 2 or f == 3:
    print ("prime")
    jj = 1
elif f == 1:
    print ("not prime")
    jj = 1


if f % 2 == 0 and jj == 0 :
    print ("not prime")
    jj = 1
elif jj == 0 :
    for i in range (3,f) :
        
        if f % i == 0  :
            print ("not prime")
            jj = 1
            break
    if jj == 0 :

        print ("prime")












