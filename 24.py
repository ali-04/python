a = int(input())
f = dict()
f1 = list()
ae = str()

for g in range (0,a):
    f1 = input ().split()
    f[f1[0]] = f1[1]
    ae += f1[0] + '   '


t = input().split()

for n in range (0,len(t)) :
    if t[n] in ae :
        t[n] = f [t[n]]
    
j =' '.join(t)

print(j)






