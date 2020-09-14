x = int  (input ())

f = []
yy = 1



for j in range (0, x):
    f.append(input().split())
    for k in range (0,2):
        f[j][k] = int (f[j][k])
        #print(f[j][k])




for c in range (0,len(f)) :
    for cc in range (c,len(f)):
        if f [c] [0] < f [cc] [0] :
            if f [c] [1] > f [cc] [1] :
                print ("happy irsa")
                yy = 0
                break
    if yy == 0 :
        break 
            



if yy == 1 :


    print ("poor irsa")











