



bak =  lambda x,y : 1 if (x%y == 0 or y%x == 0) and not(x == 0 or y == 0 or x == 1 or y == 1) else 0




def bar_avval (y) :
    if y == 1 :
        return 0
    from math import sqrt
    vb = 0
    for zzx in range (2,int(sqrt(y)+1)):
        if bak(y ,zzx) == 1 :
            vb += 1
    if vb == 0 :
        return 1
    else:
        return 0
        





def range_avval (x,y) :
    qwe = list()
    for zx in range (x,y+1):
        vv = bar_avval (zx)
        if vv == 1 :
            qwe.append (zx)
    
    return qwe
    


def taj(y) :
    from math import sqrt
    wer = []
    oi = y
    if y == 2 :
        return [2]
    elif y == 3:
        return [3]
    elif y == 4:
        return [2,2]
    if y == 1:
        return [1]
    qp = range_avval (2,int(y/2)+1)
    if bar_avval (y) == 1:
        qp.append (y)
    for not1 in qp:
        
        while bak(oi ,not1) == 1 :
            wer.append (not1)
            oi = int (oi / not1)
    return wer


def kkm (adli) :

    tli = list()

    for q in adli:


        tli.append(taj(int(q)))


    

    ad1 = tli [0]
    ad2 = tli [1]

    bad1 = ad1
    bad2 = ad2 

    bli = list()

    for q in bad1 :

        if q in bad2 :

            bad2.remove (q)
        else:

            bli.append (q)




    i = 1

    bli = bad1 + bad2

    for q in bli :

        i *= q



    return i










def bbm (adli) :
    

    tli = list()

    for q in adli:


        tli.append(taj(int(q)))


    

    ad1 = tli [0]
    ad2 = tli [1]

    bad1 = ad1
    bad2 = ad2 

    bli = list()

    for q in bad1 :

        if q in bad2 :

            bad2.remove(q)
            bli.append(q)

    i = 1

    for q in bli :

        i *= q



    return i



w = 0




ad = input()

bb = bbm(ad.split())
kk = kkm(ad.split())
print ('%s %s'%(bb,kk))

e = 0































