s = list()
z = 0
x = 0
cc = list()

for j in range (0,10):
    sn = int(input())
    s.append (sn)
    if z < sn :
        z = sn
    
for d in s :
    if d < 2 :
        s.remove(d)


for k in range (2,round(z/2)+2):
    for t in range (2,round(k/2)+2):
        if k%t == 0 and k != t :
            x += 1
    if x == 0 :
        cc.append (k)
    x = 0

z = 0
x = 0
u = 0
#print (cc)

for ra in s :
    for ma in cc :
        if ra % ma == 0 :
            x +=1
        if ma > ra :
            break
    if x > z :
        z = x
        u = ra 
    elif x == z and ra > u :
        u = ra 
    x = 0

print (u,z)












