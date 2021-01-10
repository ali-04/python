def bigest (l):
    
    try :
        b = int(l[0])
    except:
        return None
    
    for q0 in l:
        q = int(q0)
        if q > b:
            b = q

    return b 


class Algebra :
    def __init__ (self ,power ,coefficient):
        self.power = int(power) 
        self.coef = int(coefficient)
        
    def Plus (self ,pl):
        self.coef += int(pl)
        return self 
    
    def aprence (self) :
        if self.coef >= 0 :
            return "+%iX^%i" %(self.coef,self.power)
        else:
            return "%iX^%i" %(self.coef,self.power)
    
    def multi (self ,that):
        coe = self.coef  * that.coef
        pow = self.power + that.power
        return {'coe':coe,'pow':pow}







class algebraic :

    def __init__ (self ,algebrlist):
        self.algebr = dict()
        aq = 0
        for q in algebrlist :
            self.algebr[q['pow']] = self.algebr.get(int(q['pow']),Algebra(q['pow'] ,0)).Plus(q['coe']) 
            aq += 1
        self.power = bigest (list(self.algebr.keys()))

    def aprence (self):
        sout = ''
        for q0 in self.algebr :
            q = self.algebr [q0]

            sout += '  %s' %q.aprence ()

        
        return sout 


    def multi (self,that):

        dim = []

        for q0 in self.algebr :
            q = self.algebr[q0]

            for q10 in that.algebr :
                q1 = that.algebr[q10]
                dim.append (q.multi(q1))
        
        return dim

    def apr (self):
        r = ''
        n = self.power
        for q in range(0,int(n)+1):
            r += '%s ' %str(self.algebr.get(q,Algebra(q,0)).coef) 
        
        
        return r

    def aprjson(self):
        r = []
        for q0 in self.algebr :
            q = self.algebr[q0]
            r.append({'pow':q.power,'coe':q.coef})

        return r


    def striping (self):

        algebrlist = self.aprjson()
        self.algebr = dict()

        for q in algebrlist :
            self.algebr[q['pow']] = self.algebr.get(int(q['pow']),Algebra(q['pow'] ,0)).Plus(q['coe']) 

        self.power = bigest (list(self.algebr.keys()))

        while self.algebr[self.power].coef == 0 :
            del (self.algebr[self.power])
            self.power -= 1


def multi (this,that):
    da = this.multi(that)
    return Algebra (da['power'],da['coef'])



def almulti (this,that):
    return algebraic (this.multi(that))


def Power (g,n):
    mai = almulti (g,algebraic([{'pow':0,'coe':1}]))
    dim = algebraic([{'pow':0,'coe':1}])
    for q in range(0,int(n)):
        dim = almulti (dim,mai)
    
    return dim




f0 = input().split()
f = []
for q in f0 :
    f.append(int(q))




n0 = input().split()
n = []
for q in n0 :
    n.append(int(q))


p = 0
l = list()
for q in n:
    l.append({'pow':p,'coe':q})
    p += 1

gab = algebraic(l)

j = Power(gab,f[1])
j.striping()
print (j.apr().strip())
































