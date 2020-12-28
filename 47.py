


def list_get (lis,x,y):
    if len(lis) > x :
        return lis[x]
    else:
        return y



def strl (l) :

    list =  []
    for q in l :

        list.append(str(q))
    
    return list 

















circle = [[0,1]]

satr = int(input())


num = 2

while num <= satr : 

    
    circle.append([0])

    nn = 1
    while nn <= num :
        circle[num-1].append (circle[num-2][nn-1]+list_get(circle[num-2],nn,0))

        nn += 1

        
    num += 1


for q in circle :

    print (" ".join(strl(q[1:])))