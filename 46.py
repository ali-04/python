from math import sqrt





def in2 (num):

    out = int(num) / 2
    if num % 2 == 0  :

        return int(out + 1)
    else :

        return int(out + 0.5)





def range1 (num):


    alist = list()

    for q in range(1,in2(num)):

        alist.append ([q,num-q])



    return alist 





def barr (numl) :

    numl.sort()

    if sqrt((numl[0] ** 2) + (numl[1] ** 2)) == numl[2] :
        
        return True

    else : return False




def strl (l) :

    list =  []
    for q in l :

        list.append(str(q))
    
    return list 


def range2 (num) :

    for q in range(1,num-1):

        for qq in range1 (num - q) :

            thislis = qq + [q]
            if barr (thislis) :

                thislis.sort()
                return " ".join (strl(thislis))
            


    return  "Impossible"











print (range2(int(input())))



