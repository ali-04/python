i = list()
i.append(dict({'name':'Iran'}))
i.append(dict({'name':'Spain'}))
i.append(dict({'name':'Portugal'}))
i.append(dict({'name':'Morocco'}))
v = ['Iran','Spain','Portugal','Morocco']
tar = [0,1,2,3]

def bar (a,b):
    
    r = input().split('-')
    r[0] = int(r[0])
    r[1] = int(r[1])
    if r[0] > r[1]:
        i[a] ['wins'] =  i [a].get('wins',0) + 1
        i[b] ['loses'] =  i [b].get('loses',0) + 1
        i[a] ['points'] =  i [a].get('points',0) + 3
    elif r[0] < r[1]:
        i[b] ['wins'] =  i [b].get('wins',0) + 1
        i[a] ['loses'] =  i [a].get('loses',0) + 1
        i[b] ['points'] =  i [b].get('points',0) + 3
    elif r[0] == r[1]:
        i[b] ['draws'] =  i [b].get('draws',0) + 1
        i[a] ['draws'] =  i [a].get('draws',0) + 1
        i[b] ['points'] =  i [b].get('points',0) + 1
        i[a] ['points'] =  i [a].get('points',0) + 1
    
    

    i[b] ['goal difference'] =  i [b].get('goal difference',0) + (r[1] - r[0])
    i[a] ['goal difference'] =  i [a].get('goal difference',0) + (r[0] - r[1])
    
    
    
def pr (j):
    sss = v[j] + '  ' + "wins:" +  str(i[j].get('wins',0))  + ' , ' + "loses:" + str(i[j].get('loses',0)) + ' , ' + "draws:" + str(i[j].get('draws',0)) + ' , ' + "goal difference:" + str(i[j].get('goal difference',0)) +' , ' +  'points:' + str(i[j].get('points',0))
    print (sss)





bar (0,1)
bar (0,2)
bar (0,3)
bar (1,2)
bar (1,3)
bar (2,3)

#print (i)



for g1 in range(0,4):
    for gg in range(g1,4):
        if  i [tar[gg]].get('points',0) > i [tar[g1]].get('points',0):
            hhh = tar [g1]
            tar [g1] = tar [gg]
            tar [gg] = hhh
        elif i [tar[gg]].get('points',0) == i [tar[g1]].get('points',0):
            if i [tar[gg]].get('wins',0) > i [tar[g1]].get('wins',0):
                hhh = tar [g1]
                tar [g1] = tar [gg]
                tar [gg] = hhh
            elif i [tar[gg]].get('wins',0) == i [tar[g1]].get('wins',0) and i [tar[gg]].get('name') < i [tar[g1]].get('name') :
                hhh = tar [g1]
                tar [g1] = tar [gg]
                tar [gg] = hhh
                


for f11 in range(0,4):
    f12 = tar [f11]
    pr(f12)


