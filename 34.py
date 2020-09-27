F = int(input())
a = dict()
y = str()



for r in range (0,F):
    g = input().split()
    for m in range (1,4):
        a[g[m]]=g[0]

q = input().split()

for v in q :
    if v in list(a.keys()) :
        y += a[v]+ ' '
    else :
        y += v + ' '



print (y.rstrip())



