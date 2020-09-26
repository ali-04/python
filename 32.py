s = int(input())
ef = dict()
em = dict()
vf = list()
vm = list()

for f in range (0,s):
    w = input().split('.')
    w[1] = w[1][0].upper() + w [1] [1:].lower()
    if w [0] == 'f':
        ef [w[1]] = w[2]
        vf.append (w[1])
    else :
        em [w[1]] = w[2]
        vm.append (w[1])


for q in range (0,len(vm)):
    for q1 in range (q,len(vm)):
        if vm[q] > vm[q1] :
            www = vm [q]
            vm [q] = vm [q1]
            vm [q1] = www


for q in range (0,len(vf)):
    for q1 in range (q,len(vf)):
        if vf[q] > vf[q1] :
            www = vf [q]
            vf [q] = vf [q1]
            vf [q1] = www



for aaa in vf :
    rrr = 'f' +' '+ aaa +' '+ ef [aaa]
    print (rrr)


for aaa in vm :
    rrr = 'm' +' '+ aaa +' '+ em [aaa]
    print (rrr)










