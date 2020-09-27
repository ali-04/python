j = list()
qqq = input()
yj = qqq.split('.')
er = qqq.split()
ww = {0: 0}
for vv in range(0,len(yj)):
    s = yj[vv].split()
    if vv != 0:
        ww [vv] = len(zx)
    for a in range (1,len(s)):
        f = s[a]
        if f[0] != f[0].lower():
            j.append(a+ww[vv])

    zx = s

for gg in range(0,len(j)):
    zzz = j[gg]
    eee = str(zzz+1)+':'+er[zzz]
    if eee.find('.') == -1:
        print (eee)
    else :
        eee = eee[:len(eee)-1]
        print (eee)
if j == []:
    print ('None')
