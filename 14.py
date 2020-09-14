h = input ()
l = ''
m = ""

for k in h:
    if not k == "+":
        l += k
       # print (k)

for o in range (0,  len(l)) :    
    if int (l [o]) == 1:
        m += ("1"+"+")
       # print (m)



for o in range (0,  len(l)) :    
    if int (l [o]) == 2 :
        m += ("2"+"+")
       # print (m)

for o in range (0,  len(l)) :
    if int ( l [o]) == 3 :
        m += ("3"+"+")
       # print (m)


p = len(m) - 1
print (m[:p])
































