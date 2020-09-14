i = input().split()
#print (i)

for d in range (0,len(i)):
    #print (type (i[d]))
    i[d] =   float(i[d])
    #print (type (i[d]))

#print (i)
i.sort()
#
# print (i)

s = ( (i[1]) -  (i[0])) + ( (i[2]) -  (i[1]))

if s % 1 == 0 :
    s = int (s)




print (s)



























