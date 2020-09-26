o = int(input())
da = {"Horror":0, "Romance":0, "Comedy":0, "History":0 , "Adventure":0 , "Action":0}
r = 0
u = ['Horror', 'Romance', 'Comedy', "History" , "Adventure" , "Action"]

for w in range (0,o):
    d = input().split()
    for a in range (1,4):
        da[d[a]] = da.get(d[a],0)+1
        r += 1



for x in range (0,6):
    for y in range (x,6):
        if da [u[y]] > da [u[x]]:
            fff = u[y]
            u[y] = u[x]
            u[x] = fff
        elif da [u[y]] == da [u[x]] and u[y] < u[x] :
            fff = u[y]
            u[y] = u[x]
            u[x] = fff

for pa in u :
    ddd = str(str(pa) + ' : ' + str(da[pa]))
    print (ddd)


    






















