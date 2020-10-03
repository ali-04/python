from random import randint
class ensan :
    def __init__(self,name):
        self.name = name 

class shooter(ensan) :
    pass


def rand (xx):
    a = list()
    ah = list()
    for aaa in range(0,len(xx)):
        ah.append(xx[aaa])
    vvv = len (ah)
    for zzz in range (0,vvv) :
        ttt = randint (0,len(ah)-1)
        a.append (ah[ttt])
        del (ah [ttt])
    return a




a = list()
b = list()

f = "حسین - مازیار - اکبر - نیما -  مهدی - فرهاد - محمد - خشایار - میلاد - مصطفی - امین - سعید - پویا - پوریا - رضا - علی - بهزاد - سهیل - بهروز - شهروز - سامان - محسن".split('-')

ccn = rand (f)
for www in range (0,len(ccn)) :
    if www < 11:
        a.append(shooter(ccn[www]))
        a[www].tim = 'a'
    else :
        b.append(shooter(ccn[www]))
        b[www-11].tim = 'b'



for xcv in range (0,11):
    print(a[xcv].name,a[xcv].tim)

for xcv in range (0,11):
    print(b[xcv].name,b[xcv].tim)
