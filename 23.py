t = int (input())
ma = dict()
na = list()



for y in range (0,t):
    m = input()
    
    ma [m] =  ma.get(m,0)+1

#print (len(list(ma.keys))

na = list (ma.keys())

for a in range (0,len(na)):
    for aa in range (0,len(na)):

        if na[a] < na[aa] :
            ooo = na[a]
            na [a] = na [aa]
            na[aa] = ooo


for ll in range (0,len(na)):
    print ( na[ll],ma [na[ll]])

























