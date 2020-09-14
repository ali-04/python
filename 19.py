
def gh (l):
    l = int (l)
    if not l >= 0:
        l = l * -1
        return l








asl = input().lower()

a = asl.find("ab")
b = asl.find("ba")
oo = 0

if a == -1 or b == -1 :
    print ("NO")
    oo = 1



if  abs (a - b) >= 2 and oo == 0 :
    print ('YES')  
elif oo == 0 :
    print ("NO")























