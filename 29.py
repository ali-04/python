s = list()
z = 0
x = 0
cc = list()

for j in range (0,10):
    sn = int(input())
    s.append (sn)
    if z < sn :
        z = sn
    

for k in range (2,z+1):
    for t in range (2,k+1):
        if k%t == 0 :
            x += 1
    if x == 1 :
        cc.append (k)
    x = 0




print (cc)

















