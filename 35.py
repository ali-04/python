from statistics import mean

class student:
    def __init__ (self,x,y,z):
        self.ghad = int(y)
        self.age = int(x)
        self.vazn = int(z)
    
def mean1 (cc,a,b):
    rq = list()
    for yyy in range (0,b):
        if a == 'age' :
            rte = cc[yyy].age
        elif a == 'ghad':
            rte = cc[yyy].ghad
        else :
            rte = cc[yyy].vazn
        rq.append(rte)
    return float(mean(rq))
        
        


fa = list ()
aa = list ()
bb = list ()
a = list ()
b = list ()
u = ['age' ,'ghad' ,'vazn']

def inp(x,xx):
    o = int(input())
    x.append(o)
    for q in range(0,o):
        x.append(dict())
        iii = q

    
    for ww in u:
        zzz = input().split()
        for asd in range(1,o+1):
            x [asd] [ww] = int(zzz[asd-1])
    
    for ooo in range(1,len(x)) :
        xx.append ( student(x[ooo]['age'],x[ooo]['ghad'],x[ooo]['vazn'])  )
    
    

    



inp (a,aa)
inp (b,bb)


print (mean1(aa,'age',a[0]))
print (mean1(aa,'ghad',a[0]))
print (mean1(aa,'vazn',a[0]))
print (mean1(bb,'age',b[0]))
print (mean1(bb,'ghad',b[0]))
print (mean1(bb,'vazn',b[0]))

if mean1(aa,'ghad',a[0]) != mean1(bb,'ghad',b[0]):
    if mean1(aa,'ghad',a[0]) < mean1(bb,'ghad',b[0]):
        drtd = 'B'
    else:
        drtd = 'A'
elif mean1(aa,'vazn',a[0]) != mean1(bb,'vazn',b[0]):
    if mean1(aa,'vazn',a[0]) > mean1(bb,'vazn',b[0]):
        drtd = 'B'
    else:
        drtd = 'A'
elif (mean1(aa,'ghad',a[0]) == mean1(bb,'ghad',b[0])) and (mean1(aa,'vazn',a[0]) == mean1(bb,'vazn',b[0])):
    drtd = 'Same'

print(drtd)


a = 1


