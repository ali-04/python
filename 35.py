from statistics import mean

class student:
    def __init__ (self,x,y,z):
        self.ghad = int(y)
        self.age = int(x)
        self.vazn = int(z)
        


    


fa = list ()
aa = list ()
bb = list ()
a = list ()
b = list ()
u = ['age' ,'ghad' ,'vazn']

def inp(x,xx):
    o = int(input())
    for q in range(0,o):
        x.append(dict())
        iii = q

    
    for ww in u:
        zzz = input().split()
        for asd in range(0,o):
            x [asd] [ww] = int(zzz[asd])
    
    for ooo in range(0,len(x)) :
        xx.append ( student(x[ooo]['age'],x[ooo]['ghad'],x[ooo]['vazn'])  )


inp (b,bb)
inp (a,aa)









