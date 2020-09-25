i = list()
i.append(dict())
i.append(dict())
i.append(dict())
i.append(dict())
v = ['Iran','Spain','portugal','morocco']


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









pr(1)
pr(0)
pr(2)
pr(3)




