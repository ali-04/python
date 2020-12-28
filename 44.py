def Up (word):


    if len(word) > 1:
        lword = word[0].upper() + word[1:].lower()
        return lword
    else :
        return word.upper()



def Upall (str) :

    ll = list()
    for q in str.split():

        ll.append (Up(q))
    
    return " ".join(ll)












try:
    t = int(input())
except:
    exit()

wl = list()

for q in range(0,t):

    wl.append(input())

    
for q in wl :

    print (Upall(q))










