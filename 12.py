def go (n) :
    s = 0
    for i in range (1,n+1):
        if n % i == 0 :
            s += 1
    return  (s)

h = 0             
asl = 0
        

for u in range (0 , 20):
    o =  int (input())
    ma = go (o)
    if h < ma :
       h = ma
       asl = o
    elif h == ma and o > asl :
        asl = o

           
print (asl, h)

























