def ba(dd):
    if dd != -1 :
        if dd > 90:
           exit ()
        elif dd < 10 :
           exit ()

n = input ()
n = int (n)
ba (n)

l2 = 0
b = 0


while n != -1 :

    if n >= b :
        l2 = b
        b = n
    elif n > l2 :
        l2 = n




    n = input ()
    n = int (n)
    ba (n)







print (b,l2)














